# modul for print file
def print_file(list_of_list: list, head=True):
    # check format on true
    if len(list_of_list) < 1:
        raise ValueError('Формат не валиден')
    for i in list_of_list:
        if len(i) != len(list_of_list[0]) or len(i) == 0:
            raise ValueError('Формат не валиден')

    len_table = list()
    for i in range(len(list_of_list[0])):
        ii = 0
        for st in list_of_list:
            ii = max(len(st[i]), ii)
        len_table.append(ii)
        print('-' * (sum(len_table) + 1 + 5*len(len_table)))
    if head:
        first_string = list_of_list.pop(0)
        for i, j in enumerate(first_string):
            print('|  {:^{width}}  '.format(j, width=len_table[i]), end='')
        print('|')

    for st in list_of_list:
        for f, j in enumerate(st):
            out = "|  {:" + (">" if f == len(st) - 1 else "<") + "{width}}  "
            print(out.format(j, width=len_table[f]), end='')
        print('|')
    print('-' * (sum(len_table) + 1 + 5 * len(len_table)))
