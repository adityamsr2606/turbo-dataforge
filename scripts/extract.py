import pandas as pd

def extract_sheets(excel_path, data_sheet, mbr_sheet, gearbox_sheet):

    excel = pd.ExcelFile(excel_path)

    data_df = None
    mbr_df = None
    gearbox_df = None

    # Read DATA sheet
    if data_sheet in excel.sheet_names:
        data_df = pd.read_excel(
            excel_path,
            sheet_name=data_sheet
        )

    # Read MBR sheet
    if mbr_sheet in excel.sheet_names:
        mbr_df = pd.read_excel(
            excel_path,
            sheet_name=mbr_sheet
        )

    # Read GEARBOX sheet
    if gearbox_sheet in excel.sheet_names:
        gearbox_df = pd.read_excel(
            excel_path,
            sheet_name=gearbox_sheet
        )

    return data_df, mbr_df, gearbox_df