
from pyfiglet import figlet_format
from util import create_files, create_folders
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
        num_of_files = get_num_of("files")
        file_names = get_names(num_of_files, "file")
        create_files(path_name, num_of_files, file_names)

def folders_menu():
    option = create_menu("Folders", "1. Create new folders\n2. Add files to folder")
    if option == 1:
        create_folders()

def get_names(n, s):
    file_names = []
    for _ in range(n):
        try:
            name = input(f"Enter {s} name: ")
            file_names.append(name)
        except ValueError:
            continue
    return file_names

def get_num_of(s):
    while True:
        try:
            num_of_files = int(input("How many {s}? "))
            return num_of_files
        except ValueError:
            continue

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

def create_menu(title, choices):
    title = figlet_format(title, "smslant")
    print(f"\n{title}{choices}")
    menu_option = int(input("Choose an option: "))
    return menu_option

if __name__ == "__main__":
    main()