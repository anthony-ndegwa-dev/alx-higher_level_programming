#!/usr/bin/python3

def multiple_returns(sentence):
    len_string = len(sentence)

    if (len_string == 0):
        new_tuple = (len_string, None)
    else:
        new_tuple = (len_string, sentence[0])

    return (new_tuple)
