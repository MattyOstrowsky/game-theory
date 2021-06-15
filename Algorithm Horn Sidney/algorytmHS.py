from numpy.random import randint


def index_append(graf_list) -> None:
    """
    adds indexes to the list to be searched
    :param graf_list: list of tasks to add
    :return: None
    """
    for task in graf_list:
        indexs_to_check.append(task)
    return None


def timeline(t1: int, t2: int = 0) -> None:
    """
    Adds the time of the task and the previous task to create timelines
    the time of the previous task
    :param t1: the time of the previous task
    :param t2: the time of task
    :return:
    """
    return f_czas.append(t1 + t2)


def algorytm_step(q: list) -> None:
    """
    1. finds minimal q
    2. adds more tasks to the list
    3. updates timeline
    4. removes minimal from the list
    :param q: list of q=w_i/t_i values
    :return: None
    """
    min_index = q.index(min(q))
    if indexs_to_check[min_index] <= 4:
        index_append(graf[1][indexs_to_check[min_index] - 2])

    f_index.append(indexs_to_check[min_index])
    timeline(t[indexs_to_check[min_index] - 1], f_czas[-1])
    indexs_to_check.remove(indexs_to_check[min_index])
    return None


graf = [[2, 3, 4], [[5, 6], [7, 8, 9], [10]]]
t, w = [], []
n = 10

finish = True
program = True
choose_sample = True
while program:
    while choose_sample:
        print("1. Przykład z książki")
        print("2. Losuj czas i wagi zadań")
        choose = input()
        if choose == '1':
            t = [2, 1, 3, 1, 2, 3, 3, 4, 2, 4]
            w = [3, 4, 5, 1, 4, 1, 2, 1, 1, 1]
            choose_sample = False
        elif choose == '2':
            t = [randint(1, 5) for i1 in range(n)]
            w = [randint(1, 5) for i2 in range(n)]
            choose_sample = False
        else:
            print('wybierz poprawnie !!!')

    print("zadania ")
    for i in range(10):
        print(str(i+1), end=' | ')
    print()
    print("Czas wykonywania ")
    for i in range(10):
        print(str(t[i]), end=' | ')
    print()
    print("Waga ")
    for i in range(10):
        print(str(w[i]), end=' | ')
    print()

    choose_sample = True
    f_index, f_czas = [1], [t[0]]
    indexs_to_check = []
    index_append(graf[0])

    while finish:
        algorytm_step([t[index - 1] / w[index - 1] for index in indexs_to_check])
        if not indexs_to_check:
            print('------------------------skończone------------------------')
            print("zadania w kolejności ")
            for i in range(10):
                if not i == 9:
                    print('%5s' % str(f_index[i]), end=' -> ')
                else:
                    print('%5s' % str(f_index[i]))
            print("czas ")
            for i in range(10):
                if not i == 9:
                    print('%2s' % str(f_czas[i]) + 'min', end=' -> ')
                else:
                    print('%2s' % str(f_czas[i]) + 'min')
            finish = False
    finish = True
    print('\n czy chcesz kontynuować? T/N')
    run = input()
    if run == 'N':
        program = False

