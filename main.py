
from util import create_files, create_folders, validate_path, path_exists, create_menu
import os
import sys

def main():
    while True:
        try:
            option = create_menu("Cabinet", "1. New File\n2. New Folder\n3. Quit")
            if option == 1:
                files_menu()
            elif option == 2:
                folders_menu()
            elif option == 3:
                break
            else:
                continue
        except ValueError:
            continue

def files_menu():
    option = create_menu("Files", "1. Create new files\n2. Write to file")
    if option == 1:
        path_name = get_path("files")
        file_paths = get_new_paths(path_name, "file")
        create_files(file_paths)

def folders_menu():
    option = create_menu("Folders", "1. Create new folders\n2. Add files to folder")
    if option == 1:
        path_name = get_path("folders")
        folder_paths = get_new_paths(path_name, "folder")
        create_folders(folder_paths)

def get_path(s):
    while True:
        try:
            path_name = input(f"\nEnter path to create {s}: ")  
            if validate_path(path_name) != None:
                return path_name

        except KeyboardInterrupt:
            sys.exit()

def get_new_paths(path, s):
    paths = []
    while True:
        try:
            name = input(f"{s}: ")
            if name == ".":
                return paths
            
            if not path_exists(f"{path}/{name}", paths, s):
                paths.append(f"{path}/{name}")
            else:
                continue

        except ValueError:
            continue
        except KeyboardInterrupt:
            sys.exit()


if __name__ == "__main__":
    main()