"""
Solution for day 05 of advent of code 2024
https://adventofcode.com/2024/day/05
"""
from typing import Dict, Set, List

def check_part_1(rules : Dict[int,Set[int]],update : List[int]) -> bool:
    page_set = set(update)
    n = len(update)
    for i in range(1,n):
        possible_following = rules[update[i]]
        if bool(possible_following):
            for j in range(i):
                # If an element that is located before is supposed to be located after,
                # we return False
                if update[j] in possible_following:
                    return False
    return True

def part_1(rules : Dict[int,Set[int]],updates : List[List[int]]) -> int:
    count = 0
    for update in updates:
        if check_part_1(rules,update):
            n = len(update)
            count += update[n//2]
    return count

def part_2():
    pass
