"""
CSAPX Project 1: Zipf's Law

Contains functions used across the project to aid in reading files and managing classes.

Author: Ayane Naito
"""

import csv

def read_words(file):
    reader = csv.reader(open(file))
    dict = {}
    for row in reader:
        if row[0] in dict:
            dict[row[0]] = int(dict[row[0]]) + int(row[2])
        else:
            dict[row[0]] = int(row[2])
    return dict
