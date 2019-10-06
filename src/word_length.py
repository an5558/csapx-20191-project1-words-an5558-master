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
    parser.add_argument("-o", "--output", help="display the average word lengths over years")
    parser.add_argument("-p", "--plot", help="plot the average word lengths over years")
    args = parser.parse_args()
    if os.path.isfile(args.filename):
        pass
    else:
        sys.stderr.write("Error: " + str(args.filename) + " does not exist!")

if __name__ == '__main__':
    main()