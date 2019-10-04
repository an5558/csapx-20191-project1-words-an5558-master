"""
CSAPX Project 1: Zipf's Law



Author: Ayane Naito
"""


import argparse
import sys
import os
from src import words_util

def main():
    parser = argparse.ArgumentParser
    parser.add_argument("word", help="a word to display the overall ranking of")
    parser.add_argument("filename", help="a comma separated value unigram file")
    parser.add_argument("-o", "--output", help="display the top OUTPUT (#) ranked words by number of occurrences", action="store_true")
    parser.add_argument("-p", "--plot", help="plot the word rankings from top to bottom based on occurrences", action="store_true")
    args = parser.parse.args()

if __name__ == '__main__':
    main()