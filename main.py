import gittools as git
from pathtools import get_git_folders
from yaml import safe_load

CONFIG_PATH = 'config.yml'

def load_config() -> dict | None:
    try:
        with open(CONFIG_PATH, 'r') as f:
            return safe_load(f.read())
    except:
        return None


def main() -> int:
    # Load config
    conf = load_config()
    if ( conf is None ):
        print('Could not load config.')
        return 1
    
    if ( isinstance(conf['repositories'], type(list[str])) ):
        print('Invalid repository list in config.')
        return 2
    

        


if __name__ == '__main__':
    exit(main())