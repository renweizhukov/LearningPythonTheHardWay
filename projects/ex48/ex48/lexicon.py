#!/usr/bin/env python
# -*- coding: utf-8 -*-

LEXICON_DICT = {'north': ('direction', 'north'), 
                'south': ('direction', 'south'), 
                'east': ('direction', 'east'), 
                'west': ('direction', 'west'), 
                'down': ('direction', 'down'), 
                'up': ('direction', 'up'), 
                'left': ('direction', 'left'), 
                'right': ('direction', 'right'), 
                'back': ('direction', 'back'), 
                'go': ('verb', 'go'), 
                'stop': ('verb', 'stop'), 
                'kill': ('verb', 'kill'), 
                'eat': ('verb', 'eat'), 
                'the': ('stop', 'the'),
                'in': ('stop', 'in'),
                'of': ('stop', 'of'),
                'from': ('stop', 'from'),
                'at': ('stop', 'at'),
                'it': ('stop', 'it'),
                'door': ('noun', 'door'),
                'bear': ('noun', 'bear'),
                'princess': ('noun', 'princess'),
                'cabinet': ('noun', 'cabinet')}

def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None

def scan(sentence):
    result = []

    words = sentence.split()
    for word in words:
        word_tuple = LEXICON_DICT.get(word, None)
        if word_tuple is not None:
            result.append(word_tuple)
        else:
            # Check if this word is a valid number.
            number = convert_number(word)
            if number is not None:
                number_tuple = ('number', number)
                result.append(number_tuple)
            else:
                error_tuple = ('error', word)
                result.append(error_tuple)

    return result
