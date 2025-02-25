import sys
from stats import get_words_count
from stats import get_letter_count
from stats import get_sorted_value
            
def get_book_text(file_path):
    with open(file_path) as f:
        content = f.read()
        return content

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    content = get_book_text(path)
    word_count = get_words_count(content)
    letter_count = get_letter_count(content)
    sorted_dict = get_sorted_value(letter_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print(f"----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for character_data in sorted_dict:
        print(f"{character_data['char']}: {character_data['count']}")

main()
