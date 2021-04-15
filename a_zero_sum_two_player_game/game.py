import numpy as np

file = (
    "/home/gunater/Dokumenty/"
    "A-zero-sum-two-player-game/"
    "A-zero-sum-two-player-game/sample.txt"
)


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
        result.append([float(i) for i in line])
    return np.array(result)


def find_dominant_row(data):
    for firstrow in range(len(data)):
        for secondrow in range(len(data)):
            if firstrow != secondrow:
                result = np.less_equal(data[firstrow], data[secondrow])
                if all(result):
                    data = np.delete(data, firstrow, 0)
                    return find_dominant_row(data)
    return data


def find_dominant_column(data):
    data = data.T
    for firstrow in range(len(data)):
        for secondrow in range(len(data)):
            if firstrow != secondrow:
                result = np.greater_equal(data[int(firstrow)], data[secondrow])
                if all(result):
                    data = np.delete(data, firstrow, 0)
                    return find_dominant_column(data)

    return data.T


def maxmin(data):
    list_max = []
    for row in data:
        list_max.append(min(row))
    return max(list_max), list_max.index(max(list_max)) + 1


def minmax(data):
    data = data.T
    list_min = []
    for row in data:
        list_min.append(max(row))
    return min(list_min), list_min.index(min(list_min)) + 1


def saddle_point(data):
    var_maxmin = maxmin(data)
    var_minmax = minmax(data)
    if var_maxmin == var_minmax:
        return True
    else:
        return False


data = load_data(file)
print(find_dominant_row(data))
print(find_dominant_column(data))
value, index = maxmin(data)
print(value, index)
