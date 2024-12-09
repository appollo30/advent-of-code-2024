"""
Solution for day 06 of advent of code 2024
https://adventofcode.com/2024/day/06
"""

def part_1(grid_map : str) -> int:
    inside = True
    while inside:
        inside = grid_map.update()
    return len(grid_map.visited_positions)

def part_2():
    pass
