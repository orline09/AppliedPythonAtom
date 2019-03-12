#modul for print file
def print_file(list_of_list: list, head = True):
    #check format on true
    if len(list_of_list) < 1:
        raise ValueError('Формат не валиден')
    for i in list_of_list:
        if len(i) != len(list_of_list[0]) or len(i) == 0:
            raise ValueError('Формат не валиден')

    lengths_of_table = list()
    for i in range(len(list_of_list[0])):
        ii = 0
        for strings in list_of_list:
            ii = max(len(strings[i]), ii)
        lengths_of_table.append(ii)
        print('-' * (sum(lengths_of_table) + 1 + 5*len(lengths_of_table)))
        if head:
            first_string = list_of_list.pop(0)
            for i, j in enumerate(first_string):
                print('| {:^{width}} '.format(j, width=lengths_of_table[i]), end='')
            print('|')

        for strings in list_of_list:
            for f, j in enumerate(strings):
                output = '| {:" + (">' if f == len(strings) - 1 else '<') + '{width}} '
                print(output.format(j, width=lengths[f]), end='')
            print('|')
        print('-' * (sum(lengths_of_table) + 1 + 5 * len(lengths_of_table)))


