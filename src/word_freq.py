"""
CSAPX Project 1: Zipf's Law

Computes the frequency of each word across the total occurrences of all words over all years.

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
    Adds positional and optional arguments that allow the user to specify if the user would like to display the rankings
    of overall word frequencies and their total occurrences (and up to what rank), or if they would like the results to
    be plotted using matplotlib. Runs methods needed to read the given file and calculate word frequency and ranking,
    then returns the result based on user specification.
    :return: None
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("word", help="a word to display the overall ranking of")
    parser.add_argument("filename", help="a comma separated value unigram file")
    parser.add_argument("-o", "--output", help="display the top OUTPUT (#) ranked words by number of occurrences")
    parser.add_argument("-p", "--plot", help="plot the word rankings from top to bottom based on occurrences",
                        action="store_true")
    args = parser.parse_args()
    if os.path.isfile(args.filename):
        words, total_words = words_util.read_words(args.filename)
        if args.word in words:
            word_freq = words_util.calc_freq_words(words, total_words)
            print(str(args.word) + " is ranked #" + str(words_util.calc_rank(args.word, word_freq)))
            if args.output:
                if int(args.output) <= len(word_freq):
                    for idx in range(0, int(args.output)):
                        print("#" + str(idx + 1) + ": " + str(word_freq[idx].name) + "->" + str(word_freq[idx].occ))
                else:
                    sys.stderr.write("Error: " + str(args.ouput) + " is greater than the number of words in " +
                                     str(args.filename))
            if args.plot:
                x = []
                y = []
                targetx = 0
                targety = 0
                for idx in range (0, len(word_freq)):
                    if word_freq[idx].name == args.word:
                        targetx = idx + 1
                        targety = word_freq[idx].occ
                    x.append(idx + 1)
                    y.append(word_freq[idx].occ)
                plt.loglog(x, y)
                plt.plot(targetx, targety, '*')
                plt.text(targetx, targety, args.word)
                plt.title("Word Frequencies: " + str(args.filename))
                plt.xlabel("Rank of word('" + str(args.word) + "' is rank " + str(targetx) + ")")
                plt.ylabel("Total number of Occurrences")
                plt.show()
        else:
            sys.stderr.write("Error: " + str(args.word) + " does not appear in " + str(args.filename))
    else:
        sys.stderr.write("Error: " + str(args.filename) + " does not exist!")

if __name__ == '__main__':
    main()