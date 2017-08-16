import sys
from urllib.request import urlopen


def fetch_words(url):
    with urlopen('http://sixty-north.com/c/t.txt') as story:
            story_words = []
            for line in story:
                line_words = line.decode('utf-8').split() # to convert bytes of data from http response to string
                for word in line_words:
                    story_words.append(word)
    return story_words


def print_items(items):
    for item in items:
        print(item)

# print(__name__)  # To print the name of python file


def main():
    url = sys.argv[1]
    words = fetch_words(url)
    print_items(words)


if __name__ == '__main__':
    main()

# to execute multiple functions in a module, in REPL, from words import (fetch_words, print_words)
# print_words(fetch_words())
# from words import (fetch_words, print_words, main)



