"""
CSAPX Project 1: Zipf's Law

Computes the frequency of each letter across the total occurrences of all words over all years.

Author: Ayane Naito
"""

import argparse
import sys
import os
from src import words_util
import numpy as np
import matplotlib.pyplot as plt

def main():
    """
    Adds positional and optional arguments that allow the user to specify whether the user would like the
    calculated letter frequencies to be returned via standard output or plotted using matplotlib. Runs the
    methods needed to read the given file and calculate letter frequency, then returns the result based on
    what the user specifies.
    :return: None
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="a comma separated value unigram file")
    parser.add_argument("-o", "--output", help="display letter frequencies to standard output", action="store_true")
    parser.add_argument("-p", "--plot", help="plot letter frequencies using matplotlib", action="store_true")
    args = parser.parse_args()
    if os.path.isfile(args.filename):
        letters, sum_total_letters = words_util.read_letters(args.filename)
        letter_freq = words_util.calc_freq_letters(letters, sum_total_letters)
        if args.output:
            for entry in letter_freq:
                print(entry[0] + ": " + str(entry[1]))
        if args.plot:
            x = []
            y = []
            for entry in letter_freq:
                x.append(entry.name)
                y.append(entry.freq)
            plt.bar(x, y, width=0.8)
            plt.title("Letter Frequencies: " + str(args.filename))
            plt.xlabel("Letters")
            plt.ylabel("Frequency")
            plt.show()
    else:
        sys.stderr.write("Error: " + str(args.filename) + " does not exist!")

if __name__ == '__main__':
    main()