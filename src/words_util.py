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

Word:
name (str): the word
freq (float): the frequency that the word appears in the file
occ ('int'): the total number of times that a word occurred

Year:
year (int): the year that the data of the word was collected for
occ (int): the number of times that the word has appeared in that year

Wordlen:
year (int): the year that the average word length was calculated for
avg (float): the average word length of that year
"""
Letter = collections.namedtuple('Letter', ['name', 'freq'])
Word = collections.namedtuple('Word', ['name', 'freq', 'occ'])
Year = collections.namedtuple('Year', ['year', 'occ'])
Wordlen = collections.namedtuple('Wordlen', ['year', 'avg'])
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def read_words(file):
    """
    Reads a given csv file and puts the unigrams in a dictionary with the total number of occurrences.
    :param file: The unigram file containing data on occurrences
    :return: A dictionary that uses the unigram as a key and contains the total number of occurrences of that unigram,
    an int that is the total number of words across all years recorded in the given file.
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


def read_words_years(file):
    """
    Reads a given csv file and puts the unigrams in a dictionary with the year the data came from
    and the total number of occurrences of that word for that year.
    :param file: The csv file containing the unigrams and the corresponding data
    :return: A dictionary that uses the unigram as a key and contains the year that the data for the
    word was collected from and the total number of occurrences of the word in that year.
    """
    reader = csv.reader(open(file))
    dict1 = {}
    for row in reader:
        if row[0] in dict1:
            temp = dict1[row[0]]
            temp.append(Year(
                year=int(row[1]),
                occ=int(row[2]),
            ))
            dict1[row[0]] = temp
        else:
            temp = []
            temp.append(Year(
                year=int(row[1]),
                occ=int(row[2]),
            ))
            dict1[row[0]] = temp
    return dict1


def read_letters(file):
    """
    Reads a given csv file and counts the total number of occurrences of letters in the file.
    Puts the results into a dictionary with the key as the letter.
    Counts the total number of letters in the file.
    :param file: The given csv file containing unigrams
    :return: A dictionary containing letters and their occurrences, an int value that is the sum of all letters
     in the file.
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
    Calculates the frequency that a letter appears based on a dictionary containing the number of occurrences of each
    letter and an int that is the total number of letters in the file.
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
    """
    Calculates the frequency that a word appears based on a dictionary containing the number of occurrences of
    word and an int that is the total number of words recorded in the file.
    :param dict1: A dictionary containing the number of occurrences of words in the file.
    :param total_words: An int that is the total number of words recorded in the file.
    :return: A list ordered from highest to lowest frequency containing namedtuples, which contain the word, its
    corresponding frequency, and its total number of occurrences.
    """
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
    """
    Calculates the rank of a word in an ordered list by finding the given word in the list and returning its index + 1.
    :param word: The word that the method should find the ranking for
    :param lst: The namedtuple list in which the ranking of the word should be looked for
    :return: An int that is the rank of the given word in the list
    """
    for idx in range(0, len(lst)):
        if lst[idx].name == word:
            return idx + 1

def calc_wordlen_avg(start, end, dict1):
    """
    Calculates the average word length for each year given a start year and an end year (inclusive)
    and a dictionary containing the unigrams with the year the data was collected from and the total number
    of occurrences of that word in that year.
    :param start: The starting year that the average word length should be calculated for
    :param end: The ending year that the average word length should be calculated for
    :param dict1: The dictionary that uses the unigram as a key and contains the year that the data for the
    word was collected from and the total number of occurrences of the word in that year
    :return: A list of namedtuples of years and the average word length for that year
    """
    lst = []
    for yr in range(int(start), int(end) + 1):
        sum_letters = 0
        total_words = 0
        for key in dict1:
            for entry in dict1[key]:
                if entry.year == yr:
                    sum_letters += (len(key) * entry.occ)
                    total_words += entry.occ
        lst.append(Wordlen(
            year=int(yr),
            avg=float(sum_letters/total_words),
        ))
    return lst
