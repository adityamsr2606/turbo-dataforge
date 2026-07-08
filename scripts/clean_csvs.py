import os
import pandas as pd

def clean_dataframe(df):

    # Cleaned all text columns
    for column in df.columns:

        if df[column].dtype == "object":

            df[column] = (
                df[column]
                .fillna("")
                .astype(str)
                .str.replace('"', "", regex=False)
                .str.replace("'", "", regex=False)
                .str.replace("\n", " ", regex=False)
                .str.replace("\r", " ", regex=False)
                .str.replace("\t", " ", regex=False)
                .str.replace(r"\s+", " ", regex=True)
                .str.strip()
            )

    # deep cleaning for Product Code
    for column in df.columns:

        if column.strip().lower() == "product code":

            df[column] = (
                df[column]
                .astype(str)
                .str.replace(r"\s+", "", regex=True)   # Remove ALL spaces/newlines/tabs
            )

            break

    return df


def clean_all_csvs(clean_folder):

    total = 0

    for root, _, files in os.walk(clean_folder):

        for file in files:

            # Process only original CSVs
            if not file.lower().endswith(".csv"):
                continue

            # Skip temporary files
            if file.endswith("_temp.csv"):
                continue

            csv_path = os.path.join(root, file)

            print(f"Cleaning {file}")

            df = pd.read_csv(
                csv_path,
                low_memory=False
            )

            df = clean_dataframe(df)

            temp_path = csv_path[:-4] + "_temp.csv"

            df.to_csv(
                temp_path,
                index=False,
                encoding="utf-8-sig"
            )

            os.replace(temp_path, csv_path)

            total += 1

    print(f"\nFinished cleaning {total} CSV file(s).")

if __name__ == "__main__":

    CLEAN_FOLDER = "data/cleaned_data"

    clean_all_csvs(CLEAN_FOLDER)