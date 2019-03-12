import sys

# Ваши
from FileForTools import char_encoding
from For_tsv import print_tsv
from For_json import print_json

if __name__ == '__main__':
    try:
        file_name = sys.argv[1]
        file_charset = char_encoding(file_name)
        try:
            print_json(file_name, file_charset)
        except ValueError:
            print_tsv(file_name, file_charset)
    except (FileNotFoundError, IndexError):
        print("Файл не валиден")
    except (ValueError, RuntimeError) as e:
        print(e.args[0])
