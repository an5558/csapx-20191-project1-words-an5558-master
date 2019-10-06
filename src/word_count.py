"""
CSAPX Project 1: Zipf's Law

Counts the number of occurrences of a word in a year, given the word and file containing data.

Author: Ayane Naito
"""

import argparse
import sys
import os
from src import words_util

def main():
    """
    Adds arguments that allow the user to specify the word they want the occurrences of and the
    file to search for the occurrences in. Prints out the word and the number of occurrences
    when no errors are encountered. If the file the user specifies does not exist, then an error
    message is printed saying so. If the word specified is not found in the file, an error message
    is printed saying so.
    :return: None
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("word", help="a word to display the total occurrences of")
    parser.add_argument("filename", help="a comma separated value unigram file")
    args = parser.parse_args()
    if os.path.isfile(args.filename):
        words = words_util.read_words(args.filename)[0]
        if args.word in words:
            print(args.word + ": " + str(words[args.word]))
        else:
            sys.stderr.write("Error: " + str(args.word) + " does not appear!")
    else:
        sys.stderr.write("Error: " + str(args.filename) + " does not exist!")

if __name__ == '__main__':
    main()