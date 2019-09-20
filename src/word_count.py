"""
CSAPX Project 1: Zipf's Law

Counts the number of occurences of a word in a year, given the word and file.

Author: Ayane Naito
"""

import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("word", help="a word to display the total occurrences of")
    parser.add_argument("filename", help="a comma separated value unigram file")
    args = parser.parse_args()
    print(args.word)

if __name__ == '__main__':
    main()