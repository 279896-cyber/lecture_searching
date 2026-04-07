import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    if field !=  {"unordered_numbers", "ordered_numbers", "dna_sequence"}:
        return None

    file_path = os.path.join(cwd_path, file_name)

    with open(file_path, "r") as json_file:
            data = json.load(json_file)

    return data[field]



def linear_search(sequential_data, number):
    positions = []
    count = 0
    idx = 0
    while idx < len(sequential_data):
        if sequential_data[idx] == number:

            positions.append(idx)
            count += 1
        idx += 1

    return {

        "positions": positions,
        "count": count
    }

def binary_search(ordered_numbers, number):
    left = 0
    right = len(ordered_numbers)-1
    while left <= right:
        pulka = (left + right) //2

        if number








def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    vysledek = linear_search(sequential_data, 20)
    print(vysledek)

if __name__ == '__main__':
    main()