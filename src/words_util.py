"""
CSAPX Project 1: Zipf's Law

Contains functions used across the project to aid in reading files and managing classes.

Author: Ayane Naito
"""

import csv

def read_words(file):
    """
    Reads a given csv file and puts the unigrams in a dictionary with the total number of occurrences.
    :param file: The unigram file containing data on occurrences
    :return: A dictionary that uses the unigram as a key and contains the total number of occurrences of that unigram
    """
    reader = csv.reader(open(file))
    dict = {}
    for row in reader:
        if row[0] in dict:
            dict[row[0]] = int(dict[row[0]]) + int(row[2])
        else:
            dict[row[0]] = int(row[2])
    return dict
