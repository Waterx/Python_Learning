# -*- coding: utf-8 -*-
direction = ('north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back')
verb = ('go', 'stop', 'kill', 'eat')
stop = ('the', 'in', 'of', 'from', 'at', 'it')
noun = ('door', 'bear', 'princess', 'cabinet')

def def_num(word):
    try:
        return int(word)
    except ValueError:
        return False

def def_type(word):
    if word in direction:
        return ('direction', word)
    elif word in verb:
        return ('verb', word)
    elif word in stop:
        return ('stop', word)
    elif word in noun:
        return ('noun', word)
    elif def_num(word):
        return ('number', int(word))
    else:
        return ('error', word)

def scan(words):
    words_list = words.split()
    words_list_token = []
    for word in words_list:
        words_list_token.append(def_type(word))
    return words_list_token