import functions


def find_last_nodes_values(last_part_table):
    dic_distances = {last_part_table[0][3]: 0}
    dic_connections = {last_part_table[0][3]: 'null'}
    for i in range(len(last_part_table)):
        if last_part_table[i][3] not in dic_distances.keys():
            dic_distances[last_part_table[i][3]] = 0
            dic_connections[last_part_table[i][3]] = 'null'
    return dic_distances, dic_connections


def one_node_process(dictionary_distances, dictionary_connections, one_node_table):
    temp_table = []
    for i in range(len(one_node_table)):
        temp_table.append(int(one_node_table[i][4]) + int(dictionary_distances[one_node_table[i][3]]))

    dictionary_distances[one_node_table[0][1]] = max(temp_table)
    dictionary_connections[one_node_table[0][1]] = one_node_table[temp_table.index(max(temp_table))][2]
    return dictionary_distances, dictionary_connections


def find_next_nodes_connected(data, dictionary_connections, max_first_part_index):
    nulls = functions.indexes_of_nulls(dictionary_connections)
    indexes = []
    index = max_first_part_index
    indexes.append(index)
    while index not in nulls:
        temp = index
        index = functions.find_connection_by_letter(data, dictionary_connections[temp])
        indexes.append(index)

    return indexes
