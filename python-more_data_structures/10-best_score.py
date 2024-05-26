#!/usr/bin/python3

def best_score(a_dictionary):
    if (a_dictionary is None or len(a_dictionary) == 0):
        return None
    best_key = list(a_dictionary.keys())[0]
    best_score = a_dictionary[best_key]
    for key, score in a_dictionary.items():
        if (score > best_score):
            best_key = key
            best_score = score
    return best_key
