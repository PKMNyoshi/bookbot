import sys
from stats import word_count, character_count, sorted_list

def get_book_text(filepath):
        # do something with f (the file) here
        with open(filepath) as f:
            # f is a file object
            file_contents = f.read()
            return file_contents  

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]

    book_text = get_book_text(filepath)
    words = word_count(book_text)
    characater = character_count(book_text)
    num_letters = character_count(book_text)
    list = sorted_list(num_letters)
    #print(list)
    print(
    f"""============ BOOKBOT ============
Analyzing book found at {filepath}...
----------- Word Count ----------
Found {words} total words
--------- Character Count -------""")
    for c in list:
        if c['char'].isalpha():
            print(f"{c['char']}: {c['count']}")
    print("============= END ===============") 

main()