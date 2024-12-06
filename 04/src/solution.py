"""
Solution for day 04 of advent of code 2024
https://adventofcode.com/2024/day/04
"""
from src.utils import spin_str, match_pattern

def part_1(word_search : str) -> int:
    """Counts the number of times the word XMAS appears in the word search
    
    Args:
        word_search (str): The word search to search in
        
    Returns:
        int: The number of times XMAS appears in the word search
    """
    kernel = "XMAS"
    kernel_diagonal = """X***
*M**
**A*
***S"""
    count = 0
    for _ in range(4):
        count += match_pattern(word_search,kernel)
        count += match_pattern(word_search,kernel_diagonal)
        kernel = spin_str(kernel)
        kernel_diagonal = spin_str(kernel_diagonal)
    return count

def part_2(word_search : str) -> int:
    """Counts the number of times the word X-MAS appears in the word search
    
    Args:
        word_search (str): The word search to search in
    
    Returns:
        int: The number of times X-MAS appears in the word search
    """
    kernel = """M*M
*A*
S*S"""
    count = 0
    for _ in range(4):
        count += match_pattern(word_search,kernel)
        kernel = spin_str(kernel)
    return count
