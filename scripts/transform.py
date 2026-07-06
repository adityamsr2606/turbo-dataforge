import pandas as pd


def create_generic_data(data_df, mbr_df, column_mapping):

    # Rename columns using mapping
    if column_mapping:
        if data_df is not None:
            data_df = data_df.rename(columns=column_mapping)

        if mbr_df is not None:
            mbr_df = mbr_df.rename(columns=column_mapping)

    # Case 1 : Both sheets missing
    if data_df is None and mbr_df is None:
        return None

    # Case 2 : Only Data exists
    if data_df is not None and mbr_df is None:
        return data_df

    # Case 3 : Only MBR exists
    if data_df is None and mbr_df is not None:
        return mbr_df

    # Case 4 : Both exist

    # Keep Data column order
    all_columns = list(data_df.columns)

    # Add extra columns from MBR
    for col in mbr_df.columns:
        if col not in all_columns:
            all_columns.append(col)

    # Add missing columns
    data_df = data_df.reindex(
        columns=all_columns,
        fill_value=pd.NA
    )

    mbr_df = mbr_df.reindex(
        columns=all_columns,
        fill_value=pd.NA
    )

    # Append rows
    generic_df = pd.concat(
        [data_df, mbr_df],
        ignore_index=True
    )

    generic_df.reset_index(drop=True, inplace=True)

    return generic_df