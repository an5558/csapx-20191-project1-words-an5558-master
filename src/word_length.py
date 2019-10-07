"""
CSAPX Project 1: Zipf's Law

Calculates the average word length of a set of data for each year in a given range of years. Displays the
results by either printing them or plotting them using matplotlib based on user input.

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
    Adds positional and optional arguments that allow the user to specify if the user would like to display the average
    word length for each year by printing the results, or if they would like the results to be plotted using matplotlib.
    Runs methods needed to read the given file and calculate the average word length for each year, then returns the
    results based on user input.
    :return: None
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("start", help="the starting year range")
    parser.add_argument("end", help="the ending year range")
    parser.add_argument("filename", help="a comma separated value unigram file")
    parser.add_argument("-o", "--output", help="display the average word lengths over years", action="store_true")
    parser.add_argument("-p", "--plot", help="plot the average word lengths over years", action="store_true")
    args = parser.parse_args()
    if os.path.isfile(args.filename):
        words = words_util.read_words_years(args.filename)
        word_len_avg = words_util.calc_wordlen_avg(args.start, args.end, words)
        if args.output:
            for entry in word_len_avg:
                print(str(entry.year) + ": " + str(entry.avg))
        if args.plot:
            x = []
            y = []
            for entry in word_len_avg:
                x.append(entry.year)
                y.append(entry.avg)
            plt.plot(x, y)
            plt.title("Average word lengths from " + str(args.start) + " to " + str(args.end) + ": " + str(args.filename))
            plt.xlabel("Year")
            plt.ylabel("Average word length")
            plt.show()
    else:
        sys.stderr.write("Error: " + str(args.filename) + " does not exist!")

if __name__ == '__main__':
    main()