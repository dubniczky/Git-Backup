from pathlib import Path
from yaml import safe_load

from . import gitutils as git
from .utils.pathutils import get_git_folders, make_dir_tree
from .utils.termutils import color_state, print_header

CONFIG_PATH = 'config.yml'

def load_config() -> dict | None:
    try:
        with open(CONFIG_PATH, 'r') as f:
            return safe_load(f.read())
    except:
        return None


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
    target = conf['target']
    count = len(reps)
    states = []
    success_count = 0
    
    print(f'Cloning {count} repositories...')
    
    # Start backups
    for i, url in enumerate(reps):
        # Prepare
        folders, repo = get_git_folders(url)
        print_header(f'Cloning {i+1}/{count} [{repo}]')
        path = Path(target)
        
        if not conf['flatten']:
            path /= Path('/'.join(folders))
            make_dir_tree(path)
            
        # Run
        match conf['method']:
            case 'clone':
                success = git.mirror(path, url)
            case 'mirror':
                success = git.mirror(path, url)
            case _:
                print('Invalid method defined in configuration.')
                return 3
        
        # Save results
        states += [ (repo, success) ]
        if (success):
            success_count += 1
            
    # Display results
    for i,repo in enumerate(states):
        if repo[1]:
            state = color_state(' OK ', ok=True)
        else:
            state = color_state('FAIL', ok=False)
        print(f'[{state}] {repo[0]}')
    print(f'Success: {success_count} / {count}')
        
        


if __name__ == '__main__':
    exit(main())