import os

def create_file():
    dir_name = input("Enter directory to save file: ")
    file_name = input("Enter file name: ")

    try:
        with open(f"{dir_name}/{file_name}", "a"):
            pass # No content written
    except PermissionError:
        print("Permission denied")