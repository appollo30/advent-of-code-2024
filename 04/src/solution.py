"""
Solution for day 04 of advent of code 2024
https://adventofcode.com/2024/day/**
"""
import re
from typing import List
from src.utils import spin_clockwise, diagonals

def search_in_array(arr : List[str]):
    regex = r"(?<=X)MA(?=S)|(?<=S)AM(?=X)" # This regex searches for matches of XMAS or SAMX.
    # The reason it is not simply r"XMAS|SAMX" is because if there are overlappings(for instance
    # XMASAMX), the regex counts only a songle match.
    count = 0
    for line in arr:
        count += len(re.findall(regex,line))
    return count

def part_1(word_search : List[str]):
    count = 0
    count += search_in_array(word_search)
    count += search_in_array(spin_clockwise(word_search))
    count += search_in_array(diagonals(word_search))
    count += search_in_array(diagonals(spin_clockwise(word_search)))
    return count

def part_2():
    pass
