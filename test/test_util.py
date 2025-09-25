
import os
from util import create_files, create_folders

def test_create_files():
    names = ["f1", "f2", "-3123aFmei", "-.."]
    assert create_files(os.getcwd(), names) == True
    for i in names:
        os.remove(f"{os.getcwd()}/{i}")

def test_create_folders():
    names = ["games", "my-files", "py"]
    assert create_folders(os.getcwd(), names) == True
    for i in names:
        os.removedirs(f"{os.getcwd()}/{i}")
