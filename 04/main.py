"""
Day 04 of the Advent of Code 2024
https://adventofcode.com/2024/day/04
"""
from src.parser import parse
from src.solution import part_1, part_2

if __name__ == "__main__":
    FILE_NAME = "input.txt"
    word_search = parse(FILE_NAME)
    if word_search is not None:
        result_part_1 = part_1(word_search)
        print(f"Number of occurences of XMAS : {result_part_1}")
        result_part_2 = part_2(word_search)
        print(f"Number of occurences of X-MAS : {result_part_2}")
