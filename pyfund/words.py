#!/usr/bin/env python3
"""Retrieve and print words from a URL.

Usage:

     python words.py <URL>

"""
# The above is a module docstring
import sys
from urllib.request import urlopen
"""This is called docstring"""


def fetch_words(url):
    """"Fetch a list of words from URL
    Args:
        url: The URL of a UTF-8 text document
        
    Return:
        A list of strings containing the words from document
        
    """
    # The above docstring is function docstring & can be accessed from REPL by
    # from words import *
    # help(fetch_words)
    with urlopen('http://sixty-north.com/c/t.txt') as story:
            story_words = []
            for line in story:
                line_words = line.decode('utf-8').split() # to convert bytes of data from http response to string
                for word in line_words:
                    story_words.append(word)
    return story_words


def print_items(items):
    """Print items one per line
    
    Args:
        An iterable series of printable items.
    
    """
    for item in items:
        print(item)

# print(__name__)  # To print the name of python file


def main(url):
    """Print each word from a text document from a URL
    
    Args:
        URL: The URL of a UTF-8 text document. 
    """
    words = fetch_words(url)
    print_items(words)


if __name__ == '__main__':
    main(sys.argv[1])  # The 0th of the argument is name of the module file itself.

# to execute multiple functions in a module, in REPL, from words import (fetch_words, print_words)
# print_words(fetch_words())
# from words import (fetch_words, print_words, main)



