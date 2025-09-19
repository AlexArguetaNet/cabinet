import os
import sys

def create_files():
    while True:
        try:
            dir_name = input("\nEnter directory to save files\n(Press enter to use current directory): ")
            if dir_name == "":
                dir_name = os.getcwd()

            if not os.path.exists(dir_name) or not os.access(dir_name, os.W_OK):
                print("\n*****************")
                print("Directory invalid")
                print("*****************")
                continue
            else:
                num_of_files = int(input("How many files?: "))

                while num_of_files != 0:
                    file_name = input("Enter file name: ")
                    try:
                        with open(f"{dir_name}/{file_name}", "a"):
                            pass
                        num_of_files -= 1
                    except FileExistsError:
                        print("\n*********************")
                        print("File already exists")
                        print("*********************\n")
                        continue

                return
        except KeyboardInterrupt:
            sys.exit()

def create_folders():
    while True: # Run loop until valid directoy name is given
        try:
            dir_name = input("\nEnter directory to save folders\n(Press enter to use current directory): ")
            if dir_name == "": # Use current dir if input is blank
                dir_name = os.getcwd()
            
            # Check if directory exists or if permission is denied
            if not os.path.exists(dir_name) or not os.access(dir_name, os.W_OK):
                print("\n*****************")
                print("Directory invalid")
                print("*****************")
                continue
            else:
                num_of_folders = int(input("\nHow many folders?: "))

                while num_of_folders != 0: # Create number of specified folders
                    folder_name = input("Enter folder name: ")
                    try:
                        os.mkdir(f"{dir_name}/{folder_name}")
                        num_of_folders -= 1
                    except FileExistsError:
                        print("\n*********************")
                        print("Folder already exists")
                        print("*********************\n")
                        continue
                return

        except KeyboardInterrupt:
            sys.exit()