"""
Solution for day 02 of advent of code 2024
https://adventofcode.com/2024/day/2
"""
from typing import List

def part_1(reports : List[List[int]]) -> int:
    """
    Solution for part 1 of day 2,
    We go trough every report to see if the difference between report[i+1] and report[i]
    is of the same sign as report[i] and report[i-1]. To do so, we just have to multiply
    both differences together, if the product is negative, it means that they are of opposite signs.
    Then, we have to check the absolute difference between report[i+1] and report[i]. It should be
    between 1 and 3.
    If any of those conditions is not respected, we break from the loop over the report. Otherwise
    we increase the count by 1.
    **Worst-case time complexity : O(n)**
    
    Explanation :
      - If we say that n is the total number of events, then it is O(n), pretty trivial since we go 
      through every element at most two times.
    
    Args:
        reports (List[List[int]]): List of all reports

    Returns:
        int: the number of safe reports
    """
    count = 0 # The number of safe reports
    for r in reports:
        m = len(r)
        diff = 0
        for j in range(m-1):
            if (diff > 0 and r[j] > r[j+1]) or (diff < 0 and r[j] < r[j+1]):
                break
            diff = r[j+1] - r[j]
            # If diff > 0 then r is increasing between i and i+1
            # If diff < 0 then r is decreasing between i and i+1
            if abs(diff) < 1 or abs(diff) > 3:
                break
        else:
            count += 1
    return count
