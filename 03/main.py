"""
Day ** of the Advent of Code 2024
https://adventofcode.com/2024/day/**
"""
from src.parser import parse
from src.solution import part_1, part_2

if __name__ == "__main__":
    FILE_NAME = "input.txt"
    memory = parse(FILE_NAME)
    if memory is not None:
        result_part_1 = part_1(memory)
        print(f"The result of all instructions for part 1 is : {result_part_1}")
    #   result_part_2 = part_2(*)
    #   print(f"**{result_part_2}**"")
