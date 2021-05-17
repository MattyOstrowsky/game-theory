import numpy as np


def first_node_process(data):
    selected_nodes = []
    distances = []
    selected_nodes.append(1)
    selected_nodes.append((data[0].index(min(data[0])) + 1))
    distances.append(min(data[0]))

    return selected_nodes, distances


def print_values(selected_nodes, distances, distances_sum):
    print("------------------------------------------")
    # print("Aktualny stan wartości")
    print("Wybrane węzły: ", selected_nodes)
    print("Kolejne długości krawędzi: ", distances)
    print("Suma: ", distances_sum)
    print("------------------------------------------")


def find_min_and_first_index(array):
    current_min = np.amin(array)
    current_indexes = np.where(array == current_min)

    row_index = current_indexes[0][0]
    col_index = current_indexes[1][0]

    return row_index, col_index


def find_tree(data):
    selected_nodes = []
    distances = []
    distances_sum = 0
    temp_matrix = np.empty((0, len(data)))

    selected_nodes, distances = first_node_process(data)
    distances_sum = distances[0]

    # print_values(selected_nodes, distances, distances_sum)

    for i in range(len(selected_nodes)):
        temp_matrix = np.vstack([temp_matrix, data[selected_nodes[i] - 1]])

    while len(selected_nodes) != len(data):
        # print("aktualna tabela do poszukiwania wartości")
        # print(temp_matrix)
        curr_min = np.amin(temp_matrix)
        row, col = find_min_and_first_index(temp_matrix)

        if (col + 1) in selected_nodes:
            # print("to połączenie jest już uwzględnione")
            temp_matrix[row][col] = 99
        else:
            # print("można dołączać - dopisują nowy węzeł")
            selected_nodes.append(col + 1)
            distances.append(curr_min)
            distances_sum += curr_min
            temp_matrix = np.vstack([temp_matrix, data[col]])
        # print_values(selected_nodes, distances, distances_sum)

    print("Końcowy wynik:")

    print_values(selected_nodes, distances, distances_sum)
