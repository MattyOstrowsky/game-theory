import numpy as np


def load_data(file_name: str = "sample"):
    file = open(file_name)
    data, result = [], []
    try:
        for line in file.read().splitlines():
            data.append(line.split(" "))
    except Exception as e:
        print(e)
    finally:
        file.close()
    for line in data:
        result.append([i for i in line])

    array = np.array(result)
    array = make_one_symbol_in_array(array)
    array = make_empty_symbols_big_int(array)

    return_result = []

    for line in array:
        return_result.append([int(i) for i in line])

    return return_result


def make_one_symbol_in_array(array):
    for i in range(len(array)):
        for j in range(len(array)):
            element = array[i][j]
            if element == '-':
                element = 'x'
            array[j][i] = element
    return array


def make_empty_symbols_big_int(data):
    for i in range(len(data)):
        for j in range(len(data)):
            if data[i][j] == 'x':
                data[i][j] = 99
    return data
