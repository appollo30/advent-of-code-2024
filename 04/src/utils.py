"""
Utils module, contains utility functions for the project.
Contains the following functions:
- spin_str: spins a string by 90 degrees
- match_pattern: counts the number of times a pattern appears in a string
"""

def spin_str(s : str) -> str:
    """Spins a string by 90 degrees clockwise

    Args:
        s (str): The string to spin

    Returns:
        str: The spun string
    """
    lines = s.splitlines()
    n = len(lines)
    m = len(lines[0])
    result = ""
    for j in range(m):
        for i in range(n-1,-1,-1):
            result += lines[i][j]
        result += '\n'
    return result.strip()

def match_pattern(s : str,pattern : str) -> int:
    """Counts the number of times a pattern appears in a string
    The pattern can contain '*' as a wildcard character
    The pattern can be multiple lines

    Args:
        s (str): The string to search in
        pattern (str): The pattern to search for

    Returns:
        int: The number of times the pattern appears in the string
    """
    s_split = s.splitlines()
    pattern_split = pattern.splitlines()
    n = len(s_split)
    m = len(s_split[0])
    pattern_height = len(pattern_split)
    pattern_width = len(pattern_split[0])
    if pattern_height > n or pattern_width > m:
        return 0
    count = 0
    for i in range(n-pattern_height+1):
        for j in range(m-pattern_width+1):
            for k in range(pattern_height):
                for l in range(pattern_width):
                    if pattern_split[k][l] != "*" and pattern_split[k][l] != s_split[i+k][j+l]:
                        break
                else:
                    continue
                break
            else:
                count += 1
    return count
