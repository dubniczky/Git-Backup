def color_state(text, ok=True):
    res = []
    if ok:
        res += ['\033[92m'] # Green
    else:
        res += ['\033[91m'] # Red
    
    res += [text]
    res += ['\033[0m'] # Reset color
    return ''.join(res)


def print_header(text: str, pad_size=20, pad_char='=') -> None:
    pad = pad_char * pad_size
    print(f'{pad} {text} {pad}')