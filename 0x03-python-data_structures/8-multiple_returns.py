#!/usr/bin/python3
def multiple_returns(sentence):
    list_sent = len(sentence)

    if (list_sent == 0):
        new_tuple = (list_sent, None)
    else:
        new_tuple = (list_sent, sentence[0])

    return (new_tuple)
