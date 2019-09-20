"""
CSAPX Project 1: Zipf's Law

Counts the number of occurences of a word in a year, given the word and file.

Author: Ayane Naito
"""

import argparse
import sys
import os

def main():
    words = {}
    parser = argparse.ArgumentParser()
    parser.add_argument("word", help="a word to display the total occurrences of")
    parser.add_argument("filename", help="a comma separated value unigram file")
    args = parser.parse_args()
    print(args.word)
    if os.path.isfile(args.filename):
        if args.word in words:
            pass
        else:
            sys.stderr.write("Error: " + str(args.word) + " does not appear!")
    else:
       sys.stderr.write("Error: " + str(args.filename) + " does not exist!")

if __name__ == '__main__':
    main()