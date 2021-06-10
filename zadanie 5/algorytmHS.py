from numpy.random import randint


def index_append(graf_list) -> None:
    for task in graf_list:
        indexs_to_check.append(task)


def timeline(t1: int, t2: int = 0) -> None:
    f_czas.append(t1 + t2)


graf = [[2, 3, 4], [[5, 6], [7, 8, 9], [10]]]

n = 10
t = [2, 1, 3, 1, 2, 3, 3, 4, 2, 4]
w = [3, 4, 5, 1, 4, 1, 2, 1, 1, 1]
# t = [randint(1, 5) for i1 in range(n)]
# w = [randint(1, 5) for i2 in range(n)]

f_index, f_czas = [1], []
timeline(t[0])

indexs_to_check = []
index_append(graf[0])
finish = True

while finish:
    q = [t[index - 1] / w[index - 1] for index in indexs_to_check]
    print('lista f przed dodaniem')
    print(f_index)
    print('indexy do sprawdzenia')
    print(indexs_to_check)
    print('wartosci q')
    print(q)
    min_index = q.index(min(q))
    print('zadanie z wartoscia minimalna i próba dodania galezi')
    print(indexs_to_check[min_index])

    if indexs_to_check[min_index] <= 4:
        print('lista zadań do dodania')
        add = graf[1][indexs_to_check[min_index] - 2]
        print(graf[1][indexs_to_check[min_index] - 2])
        index_append(graf[1][indexs_to_check[min_index] - 2])

    f_index.append(indexs_to_check[min_index])

    timeline(t[indexs_to_check[min_index] - 1], f_czas[-1])
    print('usuniecie min index z listy do sprawdzenia')
    print(indexs_to_check[min_index])
    indexs_to_check.remove(indexs_to_check[min_index])

    print('lista indexow po usunieciu')
    print(indexs_to_check)
    print('lista zadan')
    print(f_index)

    print('koniec petli')
    if not indexs_to_check:
        print('skończone')
        finish = False

print("zadania w kolejności ")
for i in range(10):
    if not i == 9:
        print('%4s' % str(f_index[i]), end=' -> ')
    else:
        print('%4s' % str(f_index[i]))
print("czas ")
for i in range(10):
    if not i == 9:
        print('%4s' % str(f_czas[i]), end=' -> ')
    else:
        print('%4s' % str(f_czas[i]))
