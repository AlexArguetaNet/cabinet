
import builtins
import os
from util import create_files, create_folders, get_path

def test_create_files():
    assert create_files() == True

def test_create_folders():
    assert create_folders() == True

def test_get_path(monkeypatch):

    monkeypatch.setattr(builtins, "input", lambda _: os.getcwd())
    result = get_path("Files")

    assert result == os.getcwd()