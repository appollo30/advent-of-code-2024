"""
Solution for day ** of advent of code 2024
https://adventofcode.com/2024/day/**
"""
import re

def part_1(memory : str) -> int:
    regex = r"mul\((\d{,3}),(\d{,3})\)" # Regex, made it using https://regex101.com/
    # This regex is made to match text in the shape of
    # "mul(int1,int2)", where int1 and int2 are 1 to 3 digit numbers, and then group in each match
    # int1 and int2
    count = 0
    matches = re.findall(regex,memory) # Finds every pattern in the shape that is asked.
    # Outputs a list of tuples in the shape [('2', '4'), ('5', '5'), ('11', '8'), ('8', '5')]
    # Theres probably a trick to get the numbers in integer form but I haven't found it.
    for t in matches:
        count += int(t[0])*int(t[1])
    return count

def part_2(memory : str) -> int:
    count = 0
    i = 0
    n = len(memory)
    text_to_treat = ""
    capture = True
    while i < n:
        if memory[i:i+4] == "do()":
            capture = True
        elif memory[i:i+7] == "don't()":
            capture = False
        if capture:
            text_to_treat += memory[i]
        i += 1
    count += part_1(text_to_treat)
    return count
