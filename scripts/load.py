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

# Encode password (handles special characters like @)
encoded_password = quote_plus(DB_PASSWORD)

engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{encoded_password}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)


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

            df = pd.read_csv(
                csv_path,
                low_memory=False
            )

            # Store the source workbook name
            df["source_file"] = folder

            # Detect Data files
            if file.lower().endswith("_data.csv"):
                data_frames.append(df)

            # Detect Gearbox files
            elif file.lower().endswith("_gearbox.csv"):
                gearbox_frames.append(df)

    # Merge all Data files
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

    # Merge all Gearbox files
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