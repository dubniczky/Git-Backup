from requests.compat import urlsplit

def get_url_folders(url) -> tuple[list[str], str]:
    path = urlsplit(url).path.split('/')[1:]
    return (path[:-1], path[-1])