from pathlib import Path
from subprocess import run, CompletedProcess

from urllib3 import Retry

def _run(cmd: str) -> CompletedProcess:
    return run(cmd.split(' '))


# Tests if git is installed on the system
def test() -> bool:
    return _run('git --version').returncode == 0


# Clones a repository into the given folder
def clone(path: Path, url: str) -> None:
    return _run(f'cd {path} && git clone {url}').returncode == 0