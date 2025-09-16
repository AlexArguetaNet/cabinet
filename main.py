
from pyfiglet import figlet_format
import util

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
        util.create_file()

def folders_menu():
    option = create_menu("Folders", "1. Create new folders")

def create_menu(title, choices):
    title = figlet_format(title, "smslant")
    print(f"\n{title}{choices}")
    menu_option = int(input("Choose an option: "))
    return menu_option

if __name__ == "__main__":
    main()