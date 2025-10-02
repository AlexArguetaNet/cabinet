
import os
from util import create_files, create_folders, validate_path, path_exists

def test_create_files(fs):
    paths = ["/f1", "/f2", "/-3123aFmei", "/-.."]
    assert create_files(paths) == True

    for path in paths:
        assert fs.exists(path)

def test_validate_path_is_valid(fs):
    path = "/test-path"
    fs.create_dir(path)
    assert validate_path(path) == path

def test_validate_path_not_valid(fs):
    assert validate_path("/fake-path") == None

def test_path_exists_true(fs):
    path = "/test-folder"
    fs.create_dir(path)
    assert path_exists(path, [], "folders") == True
    assert path_exists(path, ["/home/user/Documents", "/test-folder"]) == True

def test_path_exists_false(fs):
    path = "/test-folder"
    assert path_exists(path, [], "folders") == False
    assert path_exists(path, ["/home/user/Documents"]) == False
    