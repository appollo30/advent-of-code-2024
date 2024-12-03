"""
Solution for day ** of advent of code 2024
https://adventofcode.com/2024/day/**
"""
from typing import List
import re

def part_1(memory : List[str]) -> int:
    regex = r"mul\((\d{,3}),(\d{,3})\)" # Regex, made it using https://regex101.com/
    count = 0
    for line in memory:
        matches = re.findall(regex,line) # Finds every pattern in the shape that is asked.
        # Outputs a list of tuples in the shape [('2', '4'), ('5', '5'), ('11', '8'), ('8', '5')]
        # Theres probably a trick to get the numbers in integer form but I haven't found it.
        for t in matches:
            count += int(t[0])*int(t[1])
    return count

def part_2():
    pass
