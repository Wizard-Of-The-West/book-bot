import sys
from stats import get_num_words, count_characters, character_report


def get_book_text(book_path):
    with open(book_path, encoding="utf-8") as f:
        book_text = f.read()
        return book_text


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book = get_book_text(book_path)

    num_words = get_num_words(book)
    num_chars = count_characters(book)
    char_report_list = character_report(num_chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in char_report_list:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


if __name__ == "__main__":
    main()
