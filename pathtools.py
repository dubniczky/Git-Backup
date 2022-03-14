from requests.compat import urlsplit
from os import makedirs
from pathlib import Path

# Extracts and separates folders and repository name from a URL
def get_git_folders(url: str) -> tuple[list[str], str]:
    path = urlsplit(url).path.split('/')[1:]
    return ( path[:-1], path[-1] )

# Creates the directories in the given path if they do not exist
def make_dir_tree(path: str | Path):
    makedirs(f'./{path}', exist_ok=True)