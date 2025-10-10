
from util import create_files, create_folders, validate_path, path_exists
from util import write_to_file, create_menu, clear
import os
import sys

def main():
    while True:
        try:
            option = create_menu("Cabinet", ["New File", "New Folder", "Quit"])
            if option == 0:
                files_menu()
            elif option == 1:
                folders_menu()
            elif option == 2:
                break
            else:
                continue
        except ValueError:
            continue
    
    clear()

def files_menu():
    option = create_menu("Files", ["Create new files", "Write to file", "Back"])
    if option == 0:
        print("Enter path to create files: ", end="")
        path_name = get_path()
        if path_name == None: return
        file_paths = get_new_paths(path_name, "file")
        create_files(file_paths)
    elif option == 1:
        file_path = input("Enter file path: ")
        write_to_file(file_path)
    else:
        return


def folders_menu():
    option = create_menu("Folders", ["Create new folders", "Add files to folder", "Back"])
    if option == 0:
        print("Enter path to create folders: ", end="")
        path_name = get_path()
        if path_name == None: return
        folder_paths = get_new_paths(path_name, "folder")
        create_folders(folder_paths)
    elif option == 1:
        # TODO: Implement function to add files to a new folder
        pass
    else:
        pass

def get_path():
    while True:
        try:
            path_name = input()  
            if validate_path(path_name) != None:
                return path_name

        except KeyboardInterrupt:
            return None

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
            return


if __name__ == "__main__":
    main()
