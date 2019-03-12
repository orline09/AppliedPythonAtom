# utf8, utf16, cp1251
# return type of encoding


def char_encoding(filename: str):
    if _is_utf16(filename):
        return 'utf16'
    elif _is_utf8(filename):
        return 'utf8'
    elif _is_cp1251(filename):
        return 'cp1251'

# try open


def _is_utf8(filename: str):
    try:
        with open(filename, encoding='utf8') as f:
            s = f.read(8)
    except UnicodeError:
        return False
    return True


def _is_utf16(filename: str):
    try:
        with open(filename, encoding='utf16') as f:
            s = f.read(8)
    except UnicodeError:
        return False
    return True
