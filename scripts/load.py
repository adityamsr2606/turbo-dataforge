import os
from urllib.parse import quote_plus

import pandas as pd
from sqlalchemy import create_engine

from config.database import (
    DB_HOST,
    DB_PORT,
    DB_NAME,
    DB_USER,
    DB_PASSWORD
)

# Encode special characters in the password
encoded_password = quote_plus(DB_PASSWORD)

# Create PostgreSQL engine
engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{encoded_password}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)


def load_cleaned_files(clean_folder):

    for folder in os.listdir(clean_folder):

        folder_path = os.path.join(clean_folder, folder)

        if not os.path.isdir(folder_path):
            continue

        for file in os.listdir(folder_path):

            if not file.endswith(".csv"):
                continue

            csv_path = os.path.join(folder_path, file)

            df = pd.read_csv(
            csv_path,
            low_memory=False
            )

            table_name = (
                f"{folder}_{os.path.splitext(file)[0]}"
                .lower()
                .replace("-", "_")
                .replace(" ", "_")
            )

            with engine.begin() as conn:
                df.to_sql(
                    name=table_name,
                    con=conn,
                    if_exists="replace",
                    index=False
                )

            print(f"Loaded table: {table_name}")

    print("\nAll cleaned CSV files have been loaded into PostgreSQL.")