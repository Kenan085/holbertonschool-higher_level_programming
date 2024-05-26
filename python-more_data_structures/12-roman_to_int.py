#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    r_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    i = 0
    while i < len(roman_string):
        current_symbol = roman_string[i]
        n_symbol = roman_string[i + 1] if i + 1 < len(roman_string) else None
        if n_symbol and r_map[current_symbol] < r_map[n_symbol]:
            result += r_map[n_symbol] - r_map[current_symbol]
            i += 2
        else:
            result += r_map[current_symbol]
            i += 1
    return result
