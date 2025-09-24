import os
import sys

# TODO: Implement function
def create_files(path_name, num_of_files, file_names):
    while num_of_files != 0:
        if not os.path.exists(f"{path_name}/{file_name}"):
            with open(f"{path_name}/{file_name}", "a"):
                pass
            num_of_files -= 1
        else:
            print("\n*********************")
            print("File already exists")
            print("*********************\n")
            continue

    return True

# TODO: Change function to accept only arguments. No user input
def create_folders():
    path_name = get_path("folders")
    num_of_folders = int(input("How many folders?: "))
    while num_of_folders != 0: # Create number of specified folders
        folder_name = input("Enter folder name: ")
        try:
            os.mkdir(f"{path_name}/{folder_name}")
            num_of_folders -= 1
        except FileExistsError:
            print("\n*********************")
            print("Folder already exists")
            print("*********************\n")
            continue
    return True


