import input_functions
import functions
import algorithm_functions


def dynamic(file):
    # file = "sample1.txt"
    data = input_functions.load_data(file)
    # oblicz ilość etapów
    max_part_number = functions.count_parts(data)
    # sub-tabela dla ostatniego etapu
    last_part_table = functions.get_part(data, max_part_number)
    # hashmapa dla krańcowych wezłów
    dictionary_distances, dictionary_connections = algorithm_functions.find_last_nodes_values(last_part_table)
    # iteracje po etapach - zapisanie kolejnych wartości dla węzłów i połączeń między nimi
    for i in reversed(range(max_part_number)):
        i = i + 1
        sub_table = functions.get_part(data, i)
        nodes_in_sub_table = functions.get_one_nodes_from_table_part(sub_table)
        for j in reversed(nodes_in_sub_table):
            sub_sub_table = functions.get_sub_table_for_node(sub_table, j)
            dictionary_distances, dictionary_connections = algorithm_functions.one_node_process(dictionary_distances,
                                                                                                dictionary_connections,
                                                                                                sub_sub_table)

    # print("wyniki pośrednie")
    # print(dictionary_distances, dictionary_connections)

    # odszukanie max wartości dla pierwszego etapu (czyli końca)
    nodes_in_sub_table = functions.get_one_nodes_from_table_part(functions.get_part(data, 1))
    temp = []
    for i in nodes_in_sub_table:
        temp.append(dictionary_distances[i])
    max_first_part = max(temp)
    max_first_part_index = functions.find_index_of_value(dictionary_distances, max_first_part)

    # jak kolejno łączą się węzły
    indexes = algorithm_functions.find_next_nodes_connected(data, dictionary_connections, max_first_part_index)

    # odczytnie liter połączeń
    letters = []
    letters.append(dictionary_connections[max_first_part_index])
    for i in range(len(indexes) - 2):
        letters.append(dictionary_connections[functions.find_connection_by_letter(data, letters[i])])
    print("Maksymalna korzyść:", max_first_part, "Dla decyzji:", letters)
    return max_first_part, letters


exit = False
while not exit:
    file = input("Podaj nazwę pliku: ")
    dynamic(file)
    option = input("Czy chcesz zakończyć działanie (T/n)?")
    if option == 't' or option == 'T':
        exit = True