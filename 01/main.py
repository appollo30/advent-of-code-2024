"""
Day 01 of the Advent of Code 2024
https://adventofcode.com/2024/day/1
"""
from src.parser import parse
from src.solution import main

if __name__ == "__main__":
    FILE_NAME = "input.txt"
    t = parse(FILE_NAME)
    if t is not None:
        list1, list2 = t
        result = main(list1,list2)
        print(f"The added distances are : {result}")
    