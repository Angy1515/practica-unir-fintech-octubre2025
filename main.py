"""
License: Apache
Organization: UNIR
"""

import os
import sys

DEFAULT_FILENAME = "words.txt"
DEFAULT_DUPLICATES = False
DEFAULT_LANGUAGE = "es"

MESSAGES = {
    "es": {
        "arg_file": "Se debe indicar el fichero como primer argumento",
        "arg_dups": "El segundo argumento indica si se quieren eliminar duplicados",
        "reading": "Se leerán las palabras del fichero",
        "not_exist": "El fichero no existe",
        "cannot_sort": "No puede ordenar",
    },
    "en": {
        "arg_file": "You must specify the file as the first argument",
        "arg_dups": "The second argument indicates whether to remove duplicates",
        "reading": "Words will be read from the file",
        "not_exist": "The file does not exist",
        "cannot_sort": "Cannot sort",
    },
}


def sort_list(items, ascending=True, lang="es"):
    if not isinstance(items, list):
        raise RuntimeError(f"{MESSAGES[lang]['cannot_sort']} {type(items)}")

    return sorted(items, reverse=(not ascending))


def remove_duplicates_from_list(items):
    return list(set(items))


if __name__ == "__main__":
    filename = DEFAULT_FILENAME
    remove_duplicates = DEFAULT_DUPLICATES
    lang = DEFAULT_LANGUAGE

    # Ejemplo de uso: python script.py words.txt yes en
    if len(sys.argv) >= 3:
        filename = sys.argv[1]
        remove_duplicates = sys.argv[2].lower() == "yes"
        if len(sys.argv) == 4:
            lang = sys.argv[3].lower()
            if lang not in MESSAGES:
                lang = DEFAULT_LANGUAGE
    else:
        print(MESSAGES[lang]["arg_file"])
        print(MESSAGES[lang]["arg_dups"])
        sys.exit(1)

    print(f"{MESSAGES[lang]['reading']} {filename}")
    file_path = os.path.join(".", filename)
    if os.path.isfile(file_path):
        word_list = []
        with open(file_path, "r") as file:
            for line in file:
                word_list.append(line.strip())
    else:
        print(f"{MESSAGES[lang]['not_exist']} {filename}")
        word_list = ["ravenclaw", "gryffindor", "slytherin", "hufflepuff"]

    if remove_duplicates:
        word_list = remove_duplicates_from_list(word_list)

    print(sort_list(word_list, lang=lang))
