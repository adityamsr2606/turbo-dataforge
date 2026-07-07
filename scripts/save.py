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

        gearbox_filename = f"{folder_name}_GEARBOX.csv"

        gearbox_path = os.path.join(
            output_folder,
            gearbox_filename
        )

        gearbox_df.to_csv(
            gearbox_path,
            index=False
        )