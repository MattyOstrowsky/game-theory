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
        result.append([i for i in line])

    return result
