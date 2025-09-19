import os
import sys

def create_files():
    path_name = get_path("files")
    num_of_files = int(input("How many files?: "))
    while num_of_files != 0:
        file_name = input("Enter file name: ")
        if not os.path.exists(f"{path_name}/{file_name}"):
            with open(f"{path_name}/{file_name}", "a"):
                pass
            num_of_files -= 1
        else:
            print("\n*********************")
            print("File already exists")
            print("*********************\n")
            continue

    return


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
    return


def get_path(s):
    while True:
        try:
            path_name = input(f"\nEnter path to create {s}: ")
            if path_name == "":
                path_name = os.getcwd()

            if not os.path.exists(path_name) or not os.access(path_name, os.W_OK):
                print("\n*****************")
                print("Directory invalid")
                print("*****************")
                continue
            else:
                return path_name

        except KeyboardInterrupt:
            sys.exit()