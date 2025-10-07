"""
License: Apache
Organization: UNIR
"""

import os
import sys

DEFAULT_FILENAME = "palabras.txt"
DEFAULT_DUPLICATES = False
DEFAULT_ASCENDING = True


def sort_list(items, ascending=True, remove_duplicates=False):
    if not isinstance(items, list):
        raise RuntimeError(f"Cannot sort {type(items)}")
    
    if remove_duplicates:
        items = list(set(items))

    return sorted(items, reverse=(not ascending))


def remove_duplicates_from_list(items):
    return list(set(items))


if __name__ == "__main__":
    filename = DEFAULT_FILENAME
    remove_duplicates = DEFAULT_DUPLICATES
    ascending = DEFAULT_ASCENDING
    
    if len(sys.argv) == 4:
        filename = sys.argv[1]
        remove_duplicates = sys.argv[2].lower() == "yes"
        ascending = sys.argv[3].lower() == "asc"
    else:
        print("Usage: python3 main.py <filename> <remove_duplicates> <order>")
        print("  filename: path to the file containing the word list, one per line")
        print("  remove_duplicates: yes|no, yes to remove duplicate words, no to keep them")
        print("  order: asc|desc, asc for ascending order, desc for descending order")
        sys.exit(1)

    print(f"Reading words from file: {filename}")
    file_path = os.path.join(".", filename)
    if os.path.isfile(file_path):
        word_list = []
        with open(file_path, "r") as file:
            for line in file:
                word_list.append(line.strip())
    else:
        print(f"File {filename} does not exist")
        word_list = ["ravenclaw", "gryffindor", "slytherin", "hufflepuff"]

    print(f"Remove duplicates: {remove_duplicates}")
    print(f"Sort order: {'ascending' if ascending else 'descending'}")
    
    result = sort_list(word_list, ascending=ascending, remove_duplicates=remove_duplicates)
    print("Sorted word list:")
    print(result)
