"""
CSAPX Project 1: Zipf's Law

Computes the frequency of each letter across the total occurrences of all words over all years.

Author: Ayane Naito
"""

import argparse
import sys
import os
from src import words_util

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="a comma separated value unigram file")
    parser.add_argument("-o", "--output", help="display letter frequencies to standard output")
    parser.add_argument("-p", "--plot", help="plot letter frequencies using matplotlib")
    args = parser.parse_args()
    if os.path.isfile(args.filename):
        letters, sum_total_letters = words_util.read_letters(args.filename)
        letter_freq = words_util.calc_frequency(letters, sum_total_letters)
        for entry in letter_freq:
            print(entry[0] + ": " + str(entry[1]))
    else:
        sys.stderr.write("Error: " + str(args.filename) + " does not exist!")

if __name__ == '__main__':
    main()