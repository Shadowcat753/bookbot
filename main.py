
def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
    return file_contents

from stats import get_word_count
from stats import count_char
from stats import sort_letters

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)

    num_words = get_word_count(book_text)
    print(f"Found {num_words} total words in the document")

    char_num = count_char(book_text)
    sorted_char = sort_letters(char_num)
    for item in sorted_char:
        char = item["char"]
        count = item["num"]
        print(f"{char}: {count}")
    

main()