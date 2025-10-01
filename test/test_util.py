
import os
from util import create_files, create_folders

def test_create_files():
    paths = [f"{os.getcwd()}/f1", f"{os.getcwd()}/f2", f"{os.getcwd()}/-3123aFmei", f"{os.getcwd()}/-.."]
    assert create_files(paths) == True
    for path in paths:
        os.remove(path)

def test_create_folders():
    paths = [f"{os.getcwd()}/games", f"{os.getcwd()}/my-files", f"{os.getcwd()}/py"]
    assert create_folders(paths) == True
    for path in paths:
        os.removedirs(path)
