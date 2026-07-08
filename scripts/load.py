from urllib.parse import quote_plus
import os
import pandas as pd
from sqlalchemy import create_engine

from config.database import (
    DB_HOST,
    DB_PORT,
    DB_NAME,
    DB_USER,
    DB_PASSWORD
)

encoded_password = quote_plus(DB_PASSWORD)

engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{encoded_password}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)


def load_single_csv(csv_path, table_name):

    if not os.path.exists(csv_path):
        print(f"{csv_path} not found.")
        return

    df = pd.read_csv(
        csv_path,
        low_memory=False
    )

    df.to_sql(
        name=table_name,
        con=engine,
        if_exists="replace",
        index=False
    )

    print(f"Loaded {table_name} table ({len(df)} rows)")


def load_cleaned_files(clean_folder):

    data_frames = []
    gearbox_frames = []

    for folder in os.listdir(clean_folder):

        folder_path = os.path.join(clean_folder, folder)

        if not os.path.isdir(folder_path):
            continue

        for file in os.listdir(folder_path):

            if not file.lower().endswith(".csv"):
                continue

            csv_path = os.path.join(folder_path, file)

            # Load Innovation Pipeline separately
            if file.lower() == "innovation_pipeline.csv":

                load_single_csv(
                    csv_path,
                    "innovation_pipeline"
                )

                continue

            # Load Protein Actual separately
            if file.lower() == "protein_actual.csv":

                load_single_csv(
                    csv_path,
                    "protein_actual"
                )

                continue

            df = pd.read_csv(
                csv_path,
                low_memory=False
            )

            # Store source workbook
            df["source_file"] = folder

            # Merge all Data CSVs
            if file.lower().endswith("_data.csv"):
                data_frames.append(df)

            # Merge all Gearbox CSVs
            elif file.lower().endswith("_gearbox.csv"):
                gearbox_frames.append(df)

    # Create DATA table
    if data_frames:

        final_data = pd.concat(
            data_frames,
            ignore_index=True,
            sort=False
        )

        final_data.to_sql(
            name="data",
            con=engine,
            if_exists="replace",
            index=False
        )

        print(f"Loaded DATA table ({len(final_data)} rows)")

    # Create GEARBOX table
    if gearbox_frames:

        final_gearbox = pd.concat(
            gearbox_frames,
            ignore_index=True,
            sort=False
        )

        final_gearbox.to_sql(
            name="gearbox",
            con=engine,
            if_exists="replace",
            index=False
        )

        print(f"Loaded GEARBOX table ({len(final_gearbox)} rows)")

    print("\nAll cleaned CSV files have been loaded into PostgreSQL.")