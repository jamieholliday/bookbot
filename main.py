import string


def count_words(text):
    words = text.split()
    return len(words)


def count_chars(text):
    lowercase_alphabet = string.ascii_lowercase
    chars = {}
    lowered = text.lower()
    for char in lowered:
        if char in chars:
            chars[char] += 1
        elif char in lowercase_alphabet:
            chars[char] = 1

    sorted_chars = sorted(chars.items(), key=lambda x: x[1], reverse=True)
    return sorted_chars


def open_file(file_name):
    with open(file_name) as file:
        text = file.read()
        return text


def print_words(file):
    word_count = count_words(file)
    print(f"{word_count} words found in the document")


def print_chars(file):
    chars = count_chars(file)
    for [key, value] in chars:
        print(f"The '{key}' character was found {value} times")


def print_report(file_name):
    file = open_file(f"./{file_name}")
    print(f"--- Begin report of {file_name} ---")
    print_words(file)
    print("")
    print_chars(file)
    print("--- End report ---")


def main():
    book = "books/frankenstein.txt"
    print_report(book)


main()
