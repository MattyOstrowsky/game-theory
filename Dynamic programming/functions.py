def get_part(table, part_number):
    ret_table = []
    boolean = False
    for i in range(len(table)):
        if boolean and table[i][0] != '-':
            break
        if boolean and table[i][0] == '-':
            ret_table.append(table[i])
        if table[i][0] == str(part_number):
            boolean = True
            ret_table.append(table[i])

    return ret_table


def count_parts(table):
    find_numbers = []
    numbers_table = []
    for i in range(len(table)):
        if table[i][0] != '-':
            find_numbers.append(table[i][0])
    for line in find_numbers:
        numbers_table.append([int(i) for i in line])

    return max(numbers_table)[0]


def get_max_node_number(last_part_table):
    maxi = last_part_table[0][3]
    for i in range(len(last_part_table)):
        if last_part_table[i][3] > maxi:
            maxi = last_part_table[i][3]

    return maxi


def get_one_nodes_from_table_part(table_part):
    nodes = []
    for i in range(len(table_part)):
        if table_part[i][1] not in nodes:
            nodes.append(table_part[i][1])
    return nodes


def get_sub_table_for_node(table_part, node):
    ret = []
    for i in range(len(table_part)):
        if table_part[i][1] == node:
            ret.append(table_part[i])
    return ret


def find_connection_by_letter(data, letter):
    for i in range(len(data)):
        if data[i][2] == letter:
            return data[i][3]


def find_index_of_value(dic, value):
    for i in dic.keys():
        if dic[i] == value:
            return i


def indexes_of_nulls(dic):
    temp = []
    for i in dic.keys():
        if 'null' == dic[i]:
            temp.append(i)
    return temp
