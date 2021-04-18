import numpy as np
from scipy.optimize import linprog


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


def linprog_A(data):
    data_transpose = data.transpose()
    negative_t_data = np.negative(data_transpose)
    b = np.ones(len(negative_t_data[0]))
    c = np.ones(len(negative_t_data))
    c = np.append(c, np.zeros(len(negative_t_data[0])))
    c = np.negative(c)
    for i in range(len(negative_t_data[0])):
        y = np.zeros(len(negative_t_data[0]))
        y[i] = -1
        negative_t_data = np.append(negative_t_data, [y], axis=0)

    res = linprog(b, A_ub=negative_t_data, b_ub=c)

    v = 0
    return_results = []

    for y in res.x:
        v += y
    v = 1 / v

    for y in res.x:
        return_results.append(v * y)
    return return_results


def linprog_B(data):
    b = np.ones(len(data[0]))
    c = np.ones(len(data))
    c = np.append(c, np.zeros(len(data[0])))
    for i in range(len(data[0])):
        y = np.zeros(len(data[0]))
        y[i] = -1
        data = np.append(data, [y], axis=0)
    res = linprog(-b, A_ub=data, b_ub=c, method="simplex")

    v = 0
    return_results = []

    for y in res.x:
        v += y
    v = 1 / v

    for y in res.x:
        return_results.append((v * y))
    return return_results
