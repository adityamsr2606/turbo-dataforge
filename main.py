from scripts.utils import load_config
from scripts.workbook_loader import load_workbooks
from scripts.extract import extract_sheets
from scripts.transform import create_generic_data
from scripts.save import save_csv
from scripts.load import load_cleaned_files
from scripts.logger import log


def main():

    # Load configuration
    config = load_config()

    raw_folder = config["raw_folder"]
    clean_folder = config["clean_folder"]

    data_sheet = config["data_sheet"]
    mbr_sheet = config["mbr_sheet"]
    gearbox_sheet = config["gearbox_sheet"]

    # Find all Excel workbooks
    workbooks = load_workbooks(raw_folder)

    log(f"{len(workbooks)} workbook(s) found.")

    # Process each workbook
    for workbook in workbooks:

        log(f"Processing {workbook['folder']}")

        data_df, mbr_df, gearbox_df = extract_sheets(
            workbook["path"],
            data_sheet,
            mbr_sheet,
            gearbox_sheet
        )

        generic_df = create_generic_data(
            data_df,
            mbr_df,
            config["column_mapping"]
        )

        save_csv(
            workbook["folder"],
            generic_df,
            gearbox_df,
            clean_folder
        )

        log(f"Finished {workbook['folder']}")

    log("All workbooks processed successfully.")

    # Load cleaned CSV files into PostgreSQL
    log("Loading cleaned CSV files into PostgreSQL...")
    load_cleaned_files(clean_folder)
    log("Database loading completed successfully.")


if __name__ == "__main__":
    main()