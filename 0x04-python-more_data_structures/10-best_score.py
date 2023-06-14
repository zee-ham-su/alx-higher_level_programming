#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    scores = sorted(a_dictionary.values(), reverse=True)
    if scores:
        return next(key for key,
                    value in a_dictionary.items() if value == scores[0])
    else:
        return None
