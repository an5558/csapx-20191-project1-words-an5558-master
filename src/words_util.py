"""
CSAPX Project 1: Zipf's Law

Contains functions used across the project to aid in reading files and managing classes.

Author: Ayane Naito
"""

import csv
import collections

"""
Letter:
name (str): the letter
freq (float): the frequency that the letter appears in the file
"""
Letter = collections.namedtuple('Letter', ['name', 'freq'])
Word = collections.namedtuple('Word', ['name', 'freq', 'occ'])
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def read_words(file):
    """
    Reads a given csv file and puts the unigrams in a dictionary with the total number of occurrences.
    :param file: The unigram file containing data on occurrences
    :return: A dictionary that uses the unigram as a key and contains the total number of occurrences of that unigram
    """
    reader = csv.reader(open(file))
    dict1 = {}
    total_words = 0
    for row in reader:
        if row[0] in dict1:
            dict1[row[0]] = int(dict1[row[0]]) + int(row[2])
            total_words += int(row[2])
        else:
            dict1[row[0]] = int(row[2])
            total_words += int(row[2])
    return dict1, total_words


def read_letters(file):
    """
    Reads a given csv file and counts the total number of occurrences of letters in the file.
    Puts the results into a dictionary with the key as the letter.
    Counts the total number of letters in the file.
    :param file: The given csv file containing unigrams
    :return: A dictionary containing letters and their occurrences, an int value that is the sum of all letters in the file.
    """
    reader = csv.reader(open(file))
    dict1 = {}
    sum_total_letters = 0
    for row in reader:
        for letter in row[0]:
            if letter in dict1:
                dict1[letter] = int(dict1[letter]) + int(row[2])
                sum_total_letters += int(row[2])
            else:
                dict1[letter] = int(row[2])
                sum_total_letters += int(row[2])
    return dict1, sum_total_letters


def calc_freq_letters(dict1, sum_total_letters):
    """
    Calculates the frequency that a letter appears based on a dictionary containing the number of occurrences of each letter
    and an int that is the total number of letters in the file.
    :param dict1: A dictionary containing the number of occurrences of each letter in the file
    :param sum_total_letters: An int that is the total number of letters in the file.
    :return: A list containing namedtuples, which contain the letter and its corresponding frequency
    """
    lst = []
    for key in alphabet:
        if key in dict1:
            lst.append(Letter(
                name=key,
                freq=float((dict1[key])/sum_total_letters),
            ))
        else:
            lst.append(Letter(
                name=key,
                freq=0.0,
            ))
    return lst


def calc_freq_words(dict1, total_words):
    lst = []
    for key in dict1:
        if len(lst) == 0:
            lst.append(Word(
                name=key,
                freq=float((dict1[key])/total_words),
                occ=int(dict1[key]),
           ))
        else:
            for idx in range(0, len(lst)):
                if dict1[key]/total_words > lst[idx].freq:
                    lst.insert(idx, Word(
                        name=key,
                        freq=float((dict1[key])/total_words),
                        occ=int(dict1[key]),
                    ))
    return lst


def calc_rank(word, lst):
    for idx in range(0, len(lst)):
        if lst[idx].name == word:
            return idx + 1
