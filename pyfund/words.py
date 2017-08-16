from urllib.request import urlopen


def fetch_words():
    with urlopen('http://sixty-north.com/c/t.txt') as story:
            story_words = []
            for line in story:
                line_words = line.decode('utf-8').split() # to convert bytes of data from http response to string
                for word in line_words:
                    story_words.append(word)
    for word in story_words:
        print(word)

# print(__name__)  # To print the name of python file

if __name__ == '__main__':
    fetch_words()

# to execute this, python words.py in REPL after doing import words



