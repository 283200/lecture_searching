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
    
    file_path = cwd_path / file_name
    with open(file_to_read, "r", encoding="utf-8") as filik:
        soubor = json.load(filik)

        if klicek not in soubor:
            return None
        return soubor[klicek]

def main():
    sequential_data = read_data('sequential.json', 'unordered_numbers')
    print(sequential_data)


if __name__ == "__main__":
    main()
