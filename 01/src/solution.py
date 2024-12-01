"""
Solution for day 01 of advent of code 2024
https://adventofcode.com/2024/day/1
"""
from typing import List
from collections import Counter

def part_1(list1 : List[int],list2 : List[int]) -> int:
    """
    Solution for part 1 of day 1,
    First we sort both lists in ascending order (or descending order can also work), 
    then we do a termwise absolute difference, and finally we sum all of those together.
    
    Worst-case time complexity : O(n*log(n)) 
    
    Explanation : The sorting of both lists is O(n*log(n)) 
    (Timsort https://en.wikipedia.org/wiki/Timsort), and the termwise sum is O(n)

    Args:
        list1 (List[int]): the first list
        list2 (List[int]): the second list

    Returns:
        int: the result of the termwise distances
    """
    n = len(list1)
    list1.sort()
    list2.sort()
    result = 0
    for i in range(n):
        result += abs(list1[i]-list2[i])
    return result

def part_2(list1 : List[int], list2 : List[int]) -> int:
    """
    Solution for part 2 of day 1,
    First we use a Counter to count the occurences of every element in list2,
    then we loop over list1 to check how many occurences of the elements of list1 in list2.
    And we finally have our result that is the product between each element of list1,
    and the number of times it appears in list2.
    
    Worst-case complexity : O(n)
    
    Explanation : The instanciation of the Counter takes O(n)
    (The size of list2)
    Then we loop over n, so still O(n).

    Args:
        list1 (List[int]): the first list
        list2 (List[int]): the second list

    Returns:
        int: the similarity between both lists
    """
    n = len(list1)
    c = Counter(list2)
    result = 0
    for i in range(n):
        element = list1[i]
        # Python counters do not raise errors if an element is not present, so we can directly
        # access it without checking if element is in c
        result += element*c[element]
    return result
