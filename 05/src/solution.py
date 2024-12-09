"""
Solution for day 05 of advent of code 2024
https://adventofcode.com/2024/day/05
"""
from typing import Dict, Set, List

def check_part_1(rules : Dict[int,Set[int]],update : List[int]) -> bool:
    """
    Check if the update is valid for part 1
    The update is valid if for every element in the update, the elements that are supposed to be
    located after are not located before.
    **Worst-case time complexity** : O(n^2)

    Explanation:
        - We iterate over the update list, and for every element, we check if the elements that are
        supposed to be located after are not located before.
        - If we find an element that is supposed to be located after, we return False

    Args:
        rules (Dict[int,Set[int]]): Dictionary that represents the rules
        update (List[int]): List of the pages in the update

    Returns:
        bool: True if the update is ordered correctly, False otherwise
    """
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
    """
    Solve part 1 of the problem
    We iterate over the updates, and for every update, we check if it is valid, and if it is, we
    add the middle element to the count.
    **Worst-case time complexity** : O(n^3)
    
    Explanation:
        - We iterate over the updates list, and for every update, we check if it is valid
        - If it is valid, we add the middle element to the count

    Args:
        rules (Dict[int,Set[int]]): Dictionary that represents the rules
        updates (List[List[int]]): List of the updates

    Returns:
        int: Sum of the middle elements of the valid updates
    """
    count = 0
    for update in updates:
        if check_part_1(rules,update):
            n = len(update)
            count += update[n//2]
    return count

def part_2(rules : Dict[int,Set[int]],updates : List[List[int]]) -> int:
    """
    Solve part 2 of the problem
    We iterate over the updates, and for every update, we check if it is valid, and if it is not, we
    add the element that is supposed to be located in the middle of the update. That is the element 
    that is supposed to be located in front of half of the elements in the update.
    **Worst-case time complexity** : O(n^3)
    
    Explanation:
        - We iterate over the updates list, and for every update, we check if it is not valid
        - If it is not valid, we add the element that is supposed to be located in the middle of the
        update. That is the element that is supposed to be located in front of half of the elements
        in the update

    Args:
        rules (Dict[int,Set[int]]): Dictionary that represents the rules
        updates (List[List[int]]): List of the updates

    Returns:
        int: Sum of the elements that are supposed to be located in the middle of the invalidupdates
    """
    # I don't know if it is considered cheating or if it is meant to be, but if we trace a graph
    # for the rules, I noticed that it is fully connected in the demo/example, so this means that
    # the position in which we should sort the array for every element, is to count the number of
    # times an element is supposed to be in front of another eleemnt in the rules dictionary.
    count = 0
    for update in updates:
        n = len(update)
        if not check_part_1(rules,update):
            update_set = set(update)
            for page in update:
                if len(rules[page].intersection(update_set)) == n//2:
                    count += page
                    break
    return count
