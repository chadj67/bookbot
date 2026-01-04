from stats import get_num_words
from stats import get_num_letters
from stats import sort_dict
import sys


def main():
    positional_args_checker()
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = word_count(book_text)
    num_letters = get_num_letters(book_text)
    sorted_letters = sort_dict(num_letters)
    print_report(book_path, num_words, sorted_letters)
    
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def word_count(book_text):
   return len(book_text.split())

def print_report(book_path, num_words, sorted_letters):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_letters:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

def positional_args_checker():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()
