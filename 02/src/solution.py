"""
Solution for day 02 of advent of code 2024
https://adventofcode.com/2024/day/2
"""
from typing import List

def helper(report : List[int]) -> bool:
    """
    We go trough the report to see if the difference between report[i+1] and report[i]
    is of the same sign as report[i] and report[i-1]. To do so, we just have to multiply
    both differences together, if the product is negative, it means that they are of opposite signs.
    Then, we have to check the absolute difference between report[i+1] and report[i]. It should be
    between 1 and 3.
    If any of those conditions is not respected, we break from the loop over the report. Otherwise
    we increase the count by 1.
    **Worst-case time complexity : O(n)**
    
    Explanation :
      - If we say that n is the number of levels, then it is O(n), pretty trivial since we loop over
      the report only once.
    
    Args:
        report (List[int]): A single report

    Returns:
        bool: ```True``` if the report is safe, ```False``` otherwise.
    """
    n = len(report)
    diff = 0
    for i in range(n-1):
        if diff*(report[i+1]-report[i]) < 0:
            return False
        diff = report[i+1] - report[i]
        # If diff > 0 then report is increasing between i and i+1
        # If diff < 0 then report is decreasing between i and i+1
        if abs(diff) < 1 or abs(diff) > 3:
            return False
    return True

def part_1(reports : List[List[int]]) -> int:
    """
    Solution for part 1 of day 2,
    We go through every single report, then count the number of times the helper function returns
    ```True```.
    **Worst-case time complexity : O(m)**
    
    Explanation :
      - If we say that m is the total number of levels, then it is O(m). We go once on every element
      for all reports, so O(m)
    
    Args:
        reports (List[List[int]]): List of all reports

    Returns:
        int: the number of safe reports
    """
    count = 0 # The number of safe reports
    for r in reports:
        if helper(r):
            count += 1
    return count

def part_2(reports : List[List[int]]) -> int:
    """
    Solution for part 2 of day 2,
    we go through every single report, then loop through the indices to check if report\\report[i]
    is safe or not using the helper function.
    **Worst-case time complexity : O(m^2)**

    Explanation :
      - If we say that m is the total number of levels, then it is O(m^2). We go through every 
      element to call the helper function, which is itself in O(n) if n is the number of levels.

    Args:
        reports (List[List[int]]): List of all reports

    Returns:
        int: the number of safe reports with the Problem Dampener.
    """
    count = 0 # The number of safe reports
    for r in reports:
        n = len(r)
        for i in range(n): # We check for every array that has the ith element removed
            if helper(r[:i]+r[i+1:]):
                count += 1
                break
    return count
