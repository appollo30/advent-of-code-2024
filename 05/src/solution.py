"""
Solution for day 05 of advent of code 2024
https://adventofcode.com/2024/day/05
"""
from typing import Dict, Set, List

def check_part_1(rules : Dict[int,Set[int]],update : List[int]) -> bool:
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

def part_2(rules : Dict[int,Set[int]],updates : List[List[int]]) -> int:
    # I don't know if it is considered cheating or if it is meant to be, but if we trace a graph
    # for the rules, I noticed that it is fully connected in the demo/example, so this means that
    # the position in which we should sort the array for every element, is to count the number of
    # times an element is supposed to be in front of another eleemnt in the rules dictionary.
    count = 0
    for update in updates:
        n = len(update)
        if not check_part_1(rules,update):
            update_set = set(update)
            update.sort(key=lambda x : len(rules[x].intersection(update_set)),reverse = True)
            count += update[n//2]
    return count
