import functions


def data():
    name_file = input("Wprowadź nazwę pliku: ")
    m = functions.load_data(name_file)
    print("Twoja macierz:")
    for s in m:
        print("wybór", *s)
    return m


def print_mini_maks(matrix: list, result: tuple):
    print("Otrzymane wyniki: ")
    for i, name in enumerate(result[0]):
        print("wybór {}: {}".format(i + 1, name))
    print(
        "Z punktu widzenia kryterium Walda najlepszą decyzją jest opcja: ",
        *result[1],
        sep=" "
    )


def print_maks_maks(matrix: list, result: tuple):
    print("Otrzymane wyniki: ")
    for i, name in enumerate(result[0]):
        print("wybór {}: {}".format(i + 1, name))
    return print(
        "Z punktu widzenia kryterium optymistycznego najlepszą decyzją jest opcja: ",
        *result[1],
        sep=" "
    )


def print_k_hurwicz(result: tuple, factor: float):
    print("Otrzymane wyniki: ")
    for i, name in enumerate(result[0]):
        print("wybór {} : {}".format(i + 1, name))
    print(
        "Z punktu widzenia kryterium Hurwicza najlepszą decyzją dla współczynnika ostrożności {} jest opcja:".format(
            factor
        ),
        *result[1],
        sep=" "
    )


def print_k_bayesa(result: tuple, prob: list):
    print("Otrzymane wyniki: ")
    for i, name in enumerate(result[0]):
        print("wybór {} : {}".format(i + 1, name))
    print(
        "Z punktu widzenia kryterium Bayesa Laplace'a najlepszą decyzją dla prawdopodobieństwa ",
        *prob,
        sep=" ",
        end=""
    )
    print(" jest opcja:", *result[1], sep=" ")


def print_k_savage(result: tuple):
    print("Otrzymane wyniki: ")
    for i, name in enumerate(result[0]):
        print("wybór {} : {}".format(i + 1, name))
    print(
        "Z punktu widzenia kryterium Savage'a najlepszą decyzją jest opcja ",
        *result[1],
        sep=" "
    )


m = data()
exit = False
while not exit:
    option = input(
        "\nWybierz kryterium podejmowania decyzji: \n"
        + "1. Krysterium minimaks\n"
        + "2. krysterium maksmaks\n"
        + "3. krysterium Hurwicza\n"
        + "4. krysterium Bayesa-Laplace'a\n"
        + "5. krysterium Savage'a\n"
        + "6. Wybierz inny plik\n"
        + "7. Wyjdź\n"
    )
    if option == "1":
        print_mini_maks(m, functions.mini_maks(m))
        input("WCISNIJ ENTER ABY COFNĄĆ")
    elif option == "2":
        print_maks_maks(m, functions.maks_maks(m))
        input("WCISNIJ ENTER ABY COFNĄĆ")
    elif option == "3":
        factor = float(input("Podaj współczynnik ostrożności: "))
        print_k_hurwicz(functions.k_hurwicz(m, factor), factor)
        input("WCISNIJ ENTER ABY COFNĄĆ")
    elif option == "4":
        prob = []
        for i in range(len(m[0]) - 1):
            prob.append(input("Podaj prawdopodobieństwo dla {} stanu: ".format(i + 1)))
        print_k_bayesa(functions.k_bayesa(m, *prob), prob)
        input("WCISNIJ ENTER ABY COFNĄĆ")
    elif option == "5":
        print_k_savage(functions.k_savage(m))
        input("WCISNIJ ENTER ABY COFNĄĆ")
    elif option == "6":
        m = data()
        input("WCISNIJ ENTER ABY COFNĄĆ")
    elif option == "7":
        exit = True
        input("WCISNIJ ENTER ABY WYJŚĆ")
    else:
        print("Nie ma takiej opcji !!")
        input("WCISNIJ ENTER ABY COFNĄĆ")
