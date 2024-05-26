#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    i = 0
    while i < len(roman_string):
        current_symbol = roman_string[i]
        next_symbol = roman_string[i + 1] if i + 1 < len(roman_string) else None
        if next_symbol and roman_map[current_symbol] < roman_map[next_symbol]:
            result += roman_map[next_symbol] - roman_map[current_symbol]
            i += 2
        else:
            result += roman_map[current_symbol]
            i += 1
    return result
