
import os
from util import create_files, create_folders, validate_path, path_exists

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

def test_validate_path_is_valid():
    path = f"{os.getcwd()}/test-path"
    os.mkdir(path)
    assert validate_path(path) == path
    os.rmdir(path)

def test_validate_path_not_valid():
    assert validate_path(f"{os.getcwd()}/fake-path") == None

def test_path_exists_true():
    path = f"{os.getcwd()}/test-folder"
    os.mkdir(path)
    assert path_exists(path, [], "folders") == True
    assert path_exists(path, ["home/user/Documents", f"{os.getcwd()}/test-folder"], "folders") == True
    os.rmdir(path)

def test_path_exists_false():
    path = f"{os.getcwd()}/test-folder"
    assert path_exists(path, [], "folders") == False
    assert path_exists(path, ["home/user/Documents"], "folders") == False
