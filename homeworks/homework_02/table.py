import sys

# our import modul
from FileForTools import char_encoding
# printing tsv
from For_tsv import print_tsv
# printing json
from For_json import print_json

if __name__ == '__main__':
    try:
        file_name = sys.argv[1]
        # check file
        Type_file = char_encoding(file_name)
        try:
            print_json(file_name, Type_file)
        except ValueError:
            print_tsv(file_name, Type_file)
    except (ValueError, RuntimeError) as e:
        print(e.args[0])
    except (FileNotFoundError, IndexError):
        print("Файл не валиден")
