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
    parser.add_argument("start", help="the starting year range")
    parser.add_argument("end", help="the ending year range")
    parser.add_argument("filename", help="a comma separated value unigram file")
    parser.add_argument("-o", "--output", help="display the average word lengths over years", action="store_true")
    parser.add_argument("-p", "--plot", help="plot the average word lengths over years", action="store_true")
    args = parser.parse_args()
    if os.path.isfile(args.filename):
        words, total_words = words_util.read_words_years(args.filename)
        word_len_avg = words_util.calc_wordlen_avg(args.start, args.end, words, total_words)
        if args.output:
            for entry in word_len_avg:
                print(str(entry.year) + ": " + str(entry.avg))
    else:
        sys.stderr.write("Error: " + str(args.filename) + " does not exist!")

if __name__ == '__main__':
    main()