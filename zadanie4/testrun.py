import input_functions
import functions
import algorithm_functions

exit = False
while not exit:
    file = "sample1.txt"
    data = input_functions.load_data(file)
    print(data)
    print("maxi")
    print(functions.count_parts(data))
    print("paty 1")
    print(functions.get_part(data, '1'))
    print("paty 2")
    print(functions.get_part(data, '2'))
    print("paty 3")
    print(functions.get_part(data, '3'))
    data_part = functions.get_part(data, '3')
    print("nodes")
    print(functions.get_max_node_number(data_part))
    print('mkbeginval')
    dictonary_d, dictonary_c = algorithm_functions.find_last_nodes_values(data_part)
    print(dictonary_d)
    print(dictonary_c)
    print("get nodes from one part")
    print(functions.get_one_nodes_from_table_part(data_part))
    print("one test subsubtable")
    one = functions.get_sub_table_for_node(data_part, functions.get_one_nodes_from_table_part(data_part)[0])
    print(one)
    print("mx")
    algorithm_functions.one_node_process(dictonary_d, dictonary_c, one)
    print("cons")
    print(functions.find_connection_by_letter(data, 'D'))

    print("NEXT")
    file = "sample2.txt"
    data = input_functions.load_data(file)
    print(data)
    print("maxi")
    print(functions.count_parts(data))
    print("paty 1")
    print(functions.get_part(data, '1'))
    print("paty 2")
    print(functions.get_part(data, '2'))
    print("paty 3")
    print(functions.get_part(data, '3'))
    data_part = functions.get_part(data, '3')
    print("nodes")
    print(functions.get_max_node_number(data_part))
    print('mkbeginval')
    dictonary_d, dictonary_c = algorithm_functions.find_last_nodes_values(data_part)
    print(dictonary_d)
    print(dictonary_c)
    print("get nodes from one part")
    print(functions.get_one_nodes_from_table_part(data_part))
    print("one test subsubtable")
    one = functions.get_sub_table_for_node(data_part, functions.get_one_nodes_from_table_part(data_part)[0])
    print(one)
    print("mx")
    algorithm_functions.one_node_process(dictonary_d, dictonary_c, one)

    exit = True