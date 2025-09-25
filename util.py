import os

def create_files(path_name, file_names):

    for i in file_names:
        with open(f"{path_name}/{i}", "a"):
            pass
    return True


def create_folders(path_name, folder_names):

    for i in folder_names:
        os.mkdir(f"{path_name}/{i}")
    return True


