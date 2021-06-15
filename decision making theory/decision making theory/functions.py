def load_data(file_name: str = 'sample1') -> list:
    file = open(file_name)
    try:
        date = file.readlines()
    except:
        print("Zły format pliku !")
    finally:
        file.close()
    matrix = []
    for line in date[1:]:
        matrix.append(line.strip().split()[:])
    return matrix


def cut_name(matrix: list) -> list:
    new_matrix = []
    for line in matrix:
        new_matrix.append(line[1:])
    return new_matrix


def loss_table(matrix: list) -> list:
    result = []
    matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    for x in range(0, len(matrix)):
        maks_list = []
        help = []
        for y in range(0, len(matrix[x])):
            maks_list.append(matrix[x][y])
        for y in range(0, len(matrix[x])):
            help.append(float(max(maks_list)) - float(matrix[x][y]))
        result.append(help)
    result = [[result[j][i] for j in range(len(result))] for i in range(len(result[0]))]
    return result


def mini_maks(matrix: list) -> tuple:
    matrix = cut_name(matrix)
    min_list = []
    result_index = []
    for mini in matrix:
        min_list.append(int(min(mini)))
    for i, num in enumerate(min_list):
        if num == max(min_list):
            result_index.append(i + 1)
    return min_list, result_index


def maks_maks(matrix: list) -> tuple:
    matrix = cut_name(matrix)
    maks_list = []
    result_index = []
    for maks in matrix:
        maks_list.append(int(max(maks)))
    for i, num in enumerate(maks_list):
        if num == max(maks_list):
            result_index.append(i + 1)
    return maks_list, result_index


def k_hurwicz(matrix: list, factor: float = 0.5) -> tuple:
    matrix = cut_name(matrix)
    result = []
    factor = float(factor)
    result_index = []
    for line in matrix:
        result.append(factor * float(min(line)) + (1 - factor) * float(max(line)))
    for i, num in enumerate(result):
        if num == max(result):
            result_index.append(i + 1)
    return result, result_index


def k_bayesa(matrix: list, *args) -> tuple:
    matrix = cut_name(matrix)
    probability = []
    result = []
    result_index = []
    for x in args:
        probability.append(x)
    for line in matrix:
        v = 0
        for x in range(len(line)):
            v += float(probability[x]) * float(line[x])
        result.append(v)
    for i, num in enumerate(result):
        if num == max(result):
            result_index.append(i + 1)
    return result, result_index


def k_savage(matrix: list) -> tuple:
    matrix = cut_name(matrix)
    matrix = loss_table(matrix)
    result = []
    result_index = []
    for line in matrix:
        result.append(max(line))
    for i, num in enumerate(result):
        if num == min(result):
            result_index.append(i + 1)
    return result, result_index
