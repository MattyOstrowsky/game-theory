import functions


def data():
    name_file = input("Wprowadź nazwę pliku: ")
    m = functions.load_data(name_file)
    print("Twoja macierz:")
    print("A/B")
    for s in m:
        print(*s)
    return m


m = data()
exit = False
while not exit:
    print("1 ETAP \nKsryterium minimaksowe")
    maxmin = functions.maxmin(m)
    minmax = functions.minmax(m)
    print(
        "Maksymalna minimalna wygrana dla gracza A wynosi: "
        + str(maxmin[0])
        + " dla strategii "
        + str(maxmin[1])
    )
    print(
        "Minimalna maksymalna przegrana dla gracza B wynosi: "
        + str(minmax[0])
        + " dla strategii "
        + str(minmax[1])
    )
    if maxmin[0] == minmax[0]:
        print("Gra posiada punkt siodłowy")
        print("Gracze wybierają strategie czyste")
        input("WCISNIJ ENTER ABY WYJŚĆ")
        exit = True
    else:
        print(
            "---Nie ma punktu siodłowego, więc nie ma rozwiązania w zbiorze strategii czystych---"
        )
        print("2 ETAP \nRedukcja macierzy")
        print("Twoja macierz zredukowana:")
        m = functions.find_dominant_column(m)
        m = functions.find_dominant_row(m)
        print("A/B")
        for s in m:
            print(*s)
        print("3 ETAP\nWyznaczenie optymalnych strategii")
        result_a = functions.linprog_A(m)
        result_b = functions.linprog_B(m)
        print("Strategia dla gracza A:")
        print([round(num, 1) for num in result_a])
        print("Strategia dla gracza B:")
        print([round(num, 1) for num in result_b])
        input("WCISNIJ ENTER ABY WYJŚĆ")
        exit = True
