"""
Day 02 of the Advent of Code 2024
https://adventofcode.com/2024/day/2
"""
from src.parser import parse
from src.solution import part_1

if __name__ == "__main__":
    FILE_NAME = "input.txt"
    reports = parse(FILE_NAME)
    if reports is not None:
        result_part_1 = part_1(reports)
        print(f"Number of safe reports : {result_part_1}")
        