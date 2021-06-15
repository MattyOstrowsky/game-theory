from TeoriaPodejmowaniaDecyzji.functions import load_data, cut_name, loss_table, mini_maks, k_hurwicz, k_bayesa, k_savage, maks_maks

sample_file = [
    "/home/gunater/Dokumenty/TPD/TeoriaPodejmowaniaDecyzji/sample1",
    "/home/gunater/Dokumenty/TPD/TeoriaPodejmowaniaDecyzji/sample2",
]


class TestFunctions:
    def test_load_data(self):

        assert load_data(sample_file[0]) == [
            ["1", "21", "15", "32", "16"],
            ["2", "28", "20", "10", "20"],
            ["3", "13", "27", "25", "15"],
            ["4", "13", "27", "25", "15"],
            ["5", "21", "15", "32", "16"],
        ]

        assert load_data(sample_file[1]) == [
            ["1", "24", "28", "36"],
            ["2", "31", "30", "28"],
            ["3", "28", "34", "29"],
            ["4", "27", "29", "33"],
            ["5", "31", "30", "29"],
        ]

    def test_cut_name(self):
        assert cut_name(load_data(sample_file[0])) == [
            ["21", "15", "32", "16"],
            ["28", "20", "10", "20"],
            ["13", "27", "25", "15"],
            ["13", "27", "25", "15"],
            ["21", "15", "32", "16"],
        ]
        assert cut_name(load_data(sample_file[1])) == [
            ["24", "28", "36"],
            ["31", "30", "28"],
            ["28", "34", "29"],
            ["27", "29", "33"],
            ["31", "30", "29"],
        ]

    def test_loss_table(self):
        assert loss_table(cut_name(load_data(sample_file[0]))) == [
            [7.0, 12.0, 0.0, 4.0],
            [0.0, 7.0, 22.0, 0.0],
            [15.0, 0.0, 7.0, 5.0],
            [15.0, 0.0, 7.0, 5.0],
            [7.0, 12.0, 0.0, 4.0],
        ]
        assert loss_table(cut_name(load_data(sample_file[1]))) == [
            [7.0, 6.0, 0.0],
            [0.0, 4.0, 8.0],
            [3.0, 0.0, 7.0],
            [4.0, 5.0, 3.0],
            [0.0, 4.0, 7.0],
        ]

    def test_mini_maks(self):
        list, index = mini_maks(load_data(sample_file[0]))
        assert list == [15, 10, 13, 13, 15] and index == [1,5] 
        list, index = mini_maks(load_data(sample_file[1]))
        assert list == [24, 28, 28, 27, 29] and index == [5] 
    
    def test_maks_maks(self):
        list, index = maks_maks(load_data(sample_file[0]))
        assert list == [32, 28, 27, 27, 32] and index == [1,5] 
        list, index = maks_maks(load_data(sample_file[1]))
        assert list == [36, 31, 34, 33, 31] and index == [1] 

    def test_k_huriwcz(self):
        list, index = k_hurwicz(load_data(sample_file[0]))
        assert list == [23.5, 19.0, 20.0, 20.0, 23.5] and index == [1,5] 
        list, index = k_hurwicz(load_data(sample_file[1]))
        assert list == [30.0, 29.5, 31.0, 30.0, 30.0] and index == [3] 

    def test_k_bayesa(self):
        list, index = k_bayesa(load_data(sample_file[0]),0.25,0.25,0.25,0.25)
        assert list == [21.0, 19.5, 20.0, 20.0, 21.0] and index == [1,5] 
        list, index = k_bayesa(load_data(sample_file[1]),0.33,0.33,0.33)
        assert list == [29.04, 29.370000000000005, 30.03, 29.37, 29.700000000000003] and index == [3] 
    
    def test_k_savage(self):
        list, index = k_savage(load_data(sample_file[0]))
        assert list == [12.0, 22.0, 15.0, 15.0, 12.0] and index == [1,5] 
        list, index = k_savage(load_data(sample_file[1]))
        assert list == [7.0, 8.0, 7.0, 5.0, 7.0] and index == [4] 