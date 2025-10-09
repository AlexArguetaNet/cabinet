import os
from pyfiglet import figlet_format
from simple_term_menu import TerminalMenu

def create_files(paths):

    for path in paths:
        with open(path, "a"):
            pass
    return True

def create_folders(paths):

    for path in paths:
        os.mkdir(path)
    return True

def validate_path(path_name):
    if path_name == "":
        return os.getcwd()

    if not os.path.exists(path_name) or not os.access(path_name, os.W_OK):
        print("\n*****************")
        print("Directory invalid")
        print("*****************")
        return None 
    else:
        return path_name

def path_exists(path, paths, s):
    if (os.path.exists(path)) or (path in paths):
        print("\n*********************")
        print(f"{s} already exists")
        print("*********************\n")
        return True
    else:
        return False

def write_to_file(file_path):
    try:
        with open(file_path, "w") as file:
            while True:
                try:
                    line = input()
                    file.write(f"{line}\n")
                except KeyboardInterrupt:
                    return True
    except IsADirectoryError:
        print("Directory entered")
        return False
    
def create_menu(title, menu_options):
    menu = TerminalMenu(menu_options, title=figlet_format(title, "smslant"))
    selected_index = menu.show()
    return selected_index