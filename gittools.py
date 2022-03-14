from pathlib import Path
from subprocess import run, CompletedProcess


def _run(cmd: str, cwd='.') -> CompletedProcess:
    return run(cmd.split(' '), cwd=cwd)


# Tests if git is installed on the system
def test() -> bool:
    return _run('git --version').returncode == 0


# Clones a repository into the given folder
def clone(path: Path, url: str) -> bool:
    return _run(f'git clone {url}', cwd=path).returncode == 0


# Pulls changes in given repository
def pull(path: Path, repo: str) -> bool:
    return _run(f'git pull', cwd=path / repo).returncode == 0