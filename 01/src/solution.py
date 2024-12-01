"""
Solution for day 01 of advent of code 2024
https://adventofcode.com/2024/day/1
"""
from typing import List

def main(list1 : List[int],list2 : List[int]) -> int:
    """
    Solution for day 1,
    First we sort both lists in ascending order (or descending order can also work), 
    then we do a termwise absolute difference, and finally we sum all of those together

    Args:
        list1 (List): the first list
        list2 (List): the second list

    Returns:
        int: the result of the termwise distances
    """
    n = len(list1)
    list1.sort()
    list2.sort()
    count = 0
    for i in range(n):
        count += abs(list1[i]-list2[i])
    return count
