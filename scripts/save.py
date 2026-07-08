import os
import pandas as pd


def clean_product_code(df):

    if df is None:
        return df

    possible_columns = [
        "Product Code",
        "Product_Code",
        "ProductCode",
        "Code",
        "SKU"
    ]

    for column in possible_columns:

        if column in df.columns:

            df[column] = (
                df[column]
                .astype(str)
                .str.replace('"', '', regex=False)
                .str.replace("'", "", regex=False)
                .str.replace("\n", "", regex=False)
                .str.replace("\r", "", regex=False)
                .str.strip()
            )

    return df


def save_csv(folder_name, generic_df, gearbox_df, clean_folder):

    output_folder = os.path.join(
        clean_folder,
        folder_name
    )

    os.makedirs(
        output_folder,
        exist_ok=True
    )

    # Save Generic Data
    if generic_df is not None:

        generic_df = clean_product_code(generic_df)

        generic_filename = f"{folder_name}_Data.csv"

        generic_path = os.path.join(
            output_folder,
            generic_filename
        )

        generic_df.to_csv(
            generic_path,
            index=False
        )

    # Save Gearbox
    if gearbox_df is not None:

        gearbox_df = clean_product_code(gearbox_df)

        gearbox_filename = f"{folder_name}_GEARBOX.csv"

        gearbox_path = os.path.join(
            output_folder,
            gearbox_filename
        )

        gearbox_df.to_csv(
            gearbox_path,
            index=False
        )