#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import os
import re


class OutputText(object):

    '''Manipulate an array into a string with different conversion methods'''

    def __init__(self, output, array):
        self.file = open(output, 'w')
        self.text = ' '.join(array)

    def format_html(self):
        '''Format string for html'''
        self.text = self.text.decode('utf-8').encode('ascii', 'xmlcharrefreplace')

    def write(self):
        self.file.write(self.text)
        self.file.close()


def random_words(directory, count):

    '''Produce an array of random words from a collection of files in a
    directory. The word count for each file is determined by the count arg'''

    words_list = []
    items = os.listdir(directory)

    for item in items:
        if not item.startswith('.'):
            txt_file = open(directory+item).readlines()
            max_length = len(txt_file)

            for i in range(count):
                    random_word = random.randint(0, max_length)
                    word_length = len(txt_file[random_word])

                    if word_length >= 5 and word_length <= 20:
                        #Split by forward slash or any white space.
                        word = re.split(r'[\s/]', txt_file[random_word])[0]

                        if '\n' in word:
                            words_list.append(word[:-1])
                        else:
                            words_list.append(word)

    random.shuffle(words_list)
    return words_list
