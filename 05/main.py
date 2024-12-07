"""
Day 05 of the Advent of Code 2024
https://adventofcode.com/2024/day/05
"""
from src.parser import parse
from src.solution import part_1, part_2

if __name__ == "__main__":
    FILE_NAME = "input.txt"
    rules, updates = parse(FILE_NAME)
    if rules is not None and updates is not None:
        result_part_1 = part_1(rules,updates)
        print(f"Result for part 1 : {result_part_1}")
        result_part_2 = part_2(rules,updates)
        print(f"Result for part 2 : {result_part_2}")
