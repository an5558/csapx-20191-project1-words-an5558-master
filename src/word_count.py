"""
CSAPX Project 1: Zipf's Law

Counts the number of occurences of a word in a year, given the word and file.

Author: Ayane Naito
"""

import argparse
import sys
import os
from src import words_util

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("word", help="a word to display the total occurrences of")
    parser.add_argument("filename", help="a comma separated value unigram file")
    args = parser.parse_args()
    if os.path.isfile(args.filename):
        words = words_util.read_words(args.filename)
        if args.word in words:
            print(args.word + ": " + str(words[args.word]))
        else:
            sys.stderr.write("Error: " + str(args.word) + " does not appear!")
    else:
        sys.stderr.write("Error: " + str(args.filename) + " does not exist!")

if __name__ == '__main__':
    main()