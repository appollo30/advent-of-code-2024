"""
Day 01 of the Advent of Code 2024
https://adventofcode.com/2024/day/1
"""
from src.parser import parse
from src.solution import part_1, part_2

if __name__ == "__main__":
    FILE_NAME = "input.txt"
    t = parse(FILE_NAME)
    if t is not None:
        list1, list2 = t
        result_part_1 = part_1(list1,list2)
        print(f"The added distances are : {result_part_1}")
        result_part_2 = part_2(list1,list2)
        print(f"The similarity between both lists is : {result_part_2}")
    