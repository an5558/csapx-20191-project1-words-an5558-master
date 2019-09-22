"""
CSAPX Project 1: Zipf's Law

Contains functions used across the project to aid in reading files and managing classes.

Author: Ayane Naito
"""

import csv
import collections

Letter = collections.namedtuple('Letter', ['name', 'freq'])

def read_words(file):
    """
    Reads a given csv file and puts the unigrams in a dictionary with the total number of occurrences.
    :param file: The unigram file containing data on occurrences
    :return: A dictionary that uses the unigram as a key and contains the total number of occurrences of that unigram
    """
    reader = csv.reader(open(file))
    dict1 = {}
    for row in reader:
        if row[0] in dict1:
            dict1[row[0]] = int(dict1[row[0]]) + int(row[2])
        else:
            dict1[row[0]] = int(row[2])
    return dict1


def read_letters(file):
    reader = csv.reader(open(file))
    dict1 = {}
    sum_total_letters = 0
    for row in reader:
        for letter in row[0]:
            if letter in dict1:
                dict1[letter] = int(dict1[letter]) + 1
                sum_total_letters += 1
            else:
                dict1[letter] = 1
                sum_total_letters += 1
    return dict1, sum_total_letters

def calc_frequency(dict1, sum_total_letters):
