from pathlib import Path
import json


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

def main():
    sequential_data = read_data('sequential.json', 'unordered_numbers')
    print(sequential_data)
    kolik=linear_search(sequential_data, 5)
    print(kolik)

if __name__ == "__main__":
    main()
