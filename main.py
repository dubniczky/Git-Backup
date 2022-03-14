import gittools as git
from pathtools import get_git_folders, make_dir_tree
from yaml import safe_load

CONFIG_PATH = 'config.yml'
TASK_HEADER_PADDING_SIZE = 15
TASK_HEADER_PADDING_CHAR = '='

def load_config() -> dict | None:
    try:
        with open(CONFIG_PATH, 'r') as f:
            return safe_load(f.read())
    except:
        return None
    
    
def print_header(text: str) -> None:
    pad = TASK_HEADER_PADDING_CHAR * TASK_HEADER_PADDING_SIZE
    print(f'{pad} {text} {pad}')


def main() -> int:
    # Load config
    print('Loading config...')
    conf = load_config()
    
    if ( conf is None ):
        print('Could not load config.')
        return 1
    
    if ( isinstance(conf['repositories'], type(list[str])) ):
        print('Invalid repository list in config.')
        return 2
    
    reps = conf['repositories']
    count = len(reps)
    
    print(f'Cloning {count} repositories...')
    
    # Start cloning
    for i, url in enumerate(reps):
        print_header(f'Cloning {i+1}/{count}')
        folders, repo = get_git_folders(url)
        make_dir_tree(Path(folders))
        
        


if __name__ == '__main__':
    exit(main())