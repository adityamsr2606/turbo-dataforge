import os


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

        generic_path = os.path.join(
            output_folder,
            "Data.csv"
        )

        generic_df.to_csv(
            generic_path,
            index=False
        )

    # Save Gearbox
    if gearbox_df is not None:

        gearbox_path = os.path.join(
            output_folder,
            "GEARBOX.csv"
        )

        gearbox_df.to_csv(
            gearbox_path,
            index=False
        )