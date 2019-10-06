"""
CSAPX Project 1: Zipf's Law



Author: Ayane Naito
"""


import argparse
import sys
import os
from src import words_util

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("word", help="a word to display the overall ranking of")
    parser.add_argument("filename", help="a comma separated value unigram file")
    parser.add_argument("-o", "--output", help="display the top OUTPUT (#) ranked words by number of occurrences")
    parser.add_argument("-p", "--plot", help="plot the word rankings from top to bottom based on occurrences", action="store_true")
    args = parser.parse_args()
    if os.path.isfile(args.filename):
        words, total_words = words_util.read_words(args.filename)
        if args.word in words:
            word_freq = words_util.calc_freq_words(words, total_words)
            print(word_freq)
            print(str(args.word) + " is ranked #" + str(words_util.calc_rank(args.word, word_freq)))
            if args.output:
                for idx in range(0, int(args.output)):
                    print("#" + str(idx + 1) + ": " + str(word_freq[idx].name) + "->" + str(word_freq[idx].occ))
        else:
            sys.stderr.write("Error: " + str(args.word) + " does not appear in " + str(args.filename))
    else:
        sys.stderr.write("Error: " + str(args.filename) + " does not exist!")

if __name__ == '__main__':
    main()