import os
import sys
from pyfiglet import figlet_format
from simple_term_menu import TerminalMenu
import getpass

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
        print("*****************\n")
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
    print("\nBegin typing to file. Press ctrl+c to exit:\n")
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
    try:
        menu = TerminalMenu(menu_options, title=figlet_format(title, "smslant"))
        selected_index = menu.show()
        return selected_index
    except KeyboardInterrupt:
        return None

def clear():
    if sys.platform.startswith("win"):
        os.system("cls")
    else:
        os.system("clear")

def success_prompt(path, names, s):
    clear()
    names_str = "\n"
    for name in names:
        names_str = f"{names_str}\n- {name}"
    names_str = f"{names_str}\n"

    menu = TerminalMenu(["Continue", "Exit"], 
                        title=f"Success!\nThe following {s} have been created in {path}:{names_str}")
    selected_index = menu.show()

    if selected_index == 0:
        return
    else:
        sys.exit()

def get_common_paths():
    user = getpass.getuser()
    if sys.platform.startswith("win"):
        common_paths = [
            f"C:\\Users\\{user}\\Documents",
            f"C:\\Users\\{user}\\Pictures",
            f"C:\\Users\\{user}\\Desktop",
            f"C:\\Users\\{user}\\Downloads"
        ]
    else:
        common_paths = [
            f"/home/{user}/Documents",
            f"/home/{user}/Downloads",
            f"/home/{user}/Desktop",
            f"/home/{user}/Pictures"
        ]
    common_paths.append("Enter custom path")
    common_paths.append("Back")
    return common_paths

def overwrite_prompt():
    menu = TerminalMenu(["Yes", "No"], title="\nOverwrite?\n")
    selected_index = menu.show()
    return selected_index