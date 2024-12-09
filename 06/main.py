"""
Day ** of the Advent of Code 2024
https://adventofcode.com/2024/day/**
"""
from src.parser import parse
from src.gridmap import GridMap
from src.solution import part_1, part_2

if __name__ == "__main__":
    FILE_NAME = "input.txt"
    grid = parse(FILE_NAME)
    if grid is not None:
        grid_map = GridMap(grid)
        result_part_1 = part_1(grid_map)
        print(f"Number of turns until out of the map : {result_part_1}")
    #   result_part_2 = part_2(*)
    #   print(f"**{result_part_2}**"")
