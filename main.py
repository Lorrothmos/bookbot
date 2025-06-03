from stats import wordcount, get_book_text, character_count, create_list
import sys

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python3 main.py <path_to_book>")
    file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    number_of_words = wordcount(book_text)
    print("============ BOOK BOT ============")
    print(f"Analyzing book found at {file_path}")
    print("------------ Word Count ------------")
    print(f"Found {number_of_words} total words")
    print("--------- Character Count ---------")
    dictionary = character_count(book_text)
    temp_dict = create_list(dictionary)
    for dict in temp_dict:
        if dict["letter"].isalpha():
            print(f"{dict["letter"]}: {dict["count"]}")
    print("============ END ============")

main()
