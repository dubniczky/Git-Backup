import pytest
from utils import pathutils
from pathlib import Path


# get_git_folders

url1 = 'https://gitlab.com/richardnagy/git-repository-auto-backup'
url2 = 'https://gitlab.com/richardnagy/git-repository-auto-backup?asd=7&b=5#fs'

def test_get_git_folders__separate():
    '''get_git_folders separation'''
    assert pathutils.get_git_folders(url1) == (['richardnagy'], 'git-repository-auto-backup')
    
def test_get_git_folders__withparams():
    '''get_git_folders with parameters'''
    assert pathutils.get_git_folders(url2) == (['richardnagy'], 'git-repository-auto-backup')
    
# make_dir_tree
    
def test_dir_tree__createlayers():
    '''make_dir_tree multiple layers'''
    target = Path('target/1/2/3')
    pathutils.make_dir_tree('target/1/2/3')
    assert target.exists()