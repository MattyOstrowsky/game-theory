import function
import inputFunctions

exit = False
while not exit:
    file = input("Podaj nazwę pliku: ")
    readed = inputFunctions.load_data(file)
    print("Wczytana macierz:")
    print(readed)
    function.find_tree(readed)
    option = input("Czy chcesz zakończyć działanie (T/n)?")
    if option == 't' or option == 'T':
        exit = True
