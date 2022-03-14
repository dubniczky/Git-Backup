from requests.compat import urlsplit

# Extracts and separates folders and repository name from a URL
def get_git_folders(url: str) -> tuple[list[str], str]:
    path = urlsplit(url).path.split('/')[1:]
    return ( path[:-1], path[-1] )