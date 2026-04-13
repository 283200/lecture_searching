from pathlib import Path
import json
import time
import matplotlib.pyplot as plt
import generators

def read_data(file_to_read, klicek):
    """
    Reads a JSON file and returns data for a given field.

    Args:
        file_name (str): Name of the JSON file.
        field (str): Key to retrieve from the JSON data.
            Must be one of: 'unordered_numbers', 'ordered_numbers' or 'dna_sequence'.

    Returns:
        list | str | None:
            - list: If data retrieved by the selected field contains numeric data.
            - str: If field is 'dna_sequence'.
            - None: If the field is not supported.
    """
    # get current working directory path
    cwd_path = Path.cwd()
    
    file_path = cwd_path / file_to_read
    with open(file_path, "r", encoding="utf-8") as filik:
        soubor = json.load(filik)

        if klicek not in soubor:
            return None
        return soubor[klicek]

def linear_search(cast, cislicko):
    indexiky=[]
    kolikrat = 0
    for i in cast:
        if i==cislicko:
            kolikrat+=1

    for indexik, y in enumerate(cast):
        if y == cislicko:
            indexiky.append(indexik)
    slovnicek={
        "position": indexiky,
        "count": kolikrat
    }
    return slovnicek
def binary_search(seznam_cisilek, cislicko):
    levacka=0
    pravacka=len(seznam_cisilek)-1
    while levacka<=pravacka:
        index1 = (levacka + pravacka) // 2
        if seznam_cisilek[index1]<cislicko:
            levacka+=1
        elif seznam_cisilek[index1]>cislicko:
            pravacka-=1
        elif seznam_cisilek[index1]==cislicko:
            return index1
    return None

def main():
    sequential_data = read_data('sequential.json', 'unordered_numbers')
    print(sequential_data)
    kolik=linear_search(sequential_data, 5)
    print(kolik)
    ord_num=read_data('sequential.json', 'ordered_numbers')
    binarka=binary_search(ord_num, -12)
    print(binarka)
    seznamek1=[]
    for u in generators:
        startik = time.perf_counter()
        linear_search(sequential_data, 5)
        endik = time.perf_counter()
        rozdilek = endik - startik
        seznamek1.append(rozdilek)
    for v in generators:
        seznamek2 = []
        startik1 = time.perf_counter()
        binary_search(ord_num, -12)
        endik1 = time.perf_counter()
        rozdilek1 = endik1 - startik1
        seznamek2.append(rozdilek1)
    print(seznamek1)
    print(seznamek2)
    plt.plot(seznamek1, seznamek2)

    plt.xlabel("Velikost vstupu")
    plt.ylabel("Čas [s]")
    plt.title("Měření času běhu")
    plt.show()
if __name__ == "__main__":
    main()
