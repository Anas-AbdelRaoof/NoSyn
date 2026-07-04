from ai_helpers import convert_pseudocode_to_code_with_ai
from file_helpers import programming_language_file, programming_language_name
from language_file_helpers import check_lang
from sys import argv, exit


def exit_if_invalid_file(name, file):
    """
    Checks for check_lang()
    """

    if check_lang(name, file) == False:
        exit()  # To avoid making incorrect file and write code in it


def write_ai_generated_code():
    """
    Takes the code from AI and writes it in your file
    """

    name = programming_language_name()
    lang_file = programming_language_file()
    exit_if_invalid_file(name, lang_file)
    code = convert_pseudocode_to_code_with_ai()
    with open(lang_file, "w") as file:
        file.write(code)  # Programming language file
