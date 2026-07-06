import os


def load_workbooks(raw_folder):

    workbooks = []

    for folder in os.listdir(raw_folder):

        folder_path = os.path.join(raw_folder, folder)

        if not os.path.isdir(folder_path):
            continue

        for file in os.listdir(folder_path):

            if file.endswith(".xlsx"):

                workbooks.append(
                    {
                        "folder": folder,
                        "path": os.path.join(folder_path, file)
                    }
                )

    return workbooks