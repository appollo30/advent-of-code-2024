"""
Solution for day 03 of advent of code 2024
https://adventofcode.com/2024/day/03
"""
import re

def part_1(memory : str) -> int:
    """
    Solution for part 1 of day 3
    We use a regex to find all occurences of shape "mul(int1,int2)" and then we multiply int1 by
    int2 and add it to the count.
    **Worst-case time complexity : O(n)**
    
    Explanation :
        - If we say that n is the number of characters in the memory string, then it is O(n). 
        We use regex to find all occurences of the pattern, which is O(n).
    
    Args:
        memory (str): The memory string

    Returns:
        int: The result of all the multiplications
    """
    regex = r"mul\((\d{,3}),(\d{,3})\)" # Regex, made it using https://regex101.com/
    # This regex is made to match text in the shape of
    # "mul(int1,int2)", where int1 and int2 are 1 to 3 digit numbers, and then group in each match
    # int1 and int2
    count = 0
    matches = re.findall(regex,memory) # Finds every pattern in the shape that is asked.
    # Outputs a list of tuples in the shape [('2', '4'), ('5', '5'), ('11', '8'), ('8', '5')]
    # Theres probably a trick to get the numbers in integer form but I haven't found it.
    for t in matches:
        count += int(t[0])*int(t[1])
    return count

def part_2(memory : str) -> int:
    """
    Solution for part 2 of day 3
    Works similarly to part 1, but we have to check if we are in a "do()" or "don't()" block.
    **Worst-case time complexity : O(n)**
    
    Explanation :
        - If we say that n is the number of characters in the memory string, then it is O(n). 
        We go through the memory string once, and then we use regex to find all occurences of
        the pattern, which is O(n)

    Args:
        memory (str): The memory string

    Returns:
        int: The result of all the multiplications after checking if we are in a "do()" or 
        "don't()" block
    """
    count = 0
    i = 0
    n = len(memory)
    text_to_treat = ""
    capture = True
    while i < n:
        if memory[i:i+4] == "do()":
            capture = True
        elif memory[i:i+7] == "don't()":
            capture = False
        if capture:
            text_to_treat += memory[i]
        i += 1
    count += part_1(text_to_treat)
    return count
