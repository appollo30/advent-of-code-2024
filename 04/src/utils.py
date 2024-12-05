from typing import List

def transpose(word_search : List[str]) -> List[str]:
    n = len(word_search)
    m = len(word_search[0])
    arr_transposed = ["".join([word_search[i][j] for i in range(n)]) for j in range(m)]
    return arr_transposed

def diagonals(word_search : List[str]) -> List[str]:
    n = len(word_search)
    m = len(word_search[0])
    result = []
    # Filling the main diagonals
    for k in range(m-1, -1, -1):
        diagonal = ""
        for j in range(k, m):
            if j - k < n:
                diagonal += word_search[j-k][j]
        result.append(diagonal)
    # Filling the anti-diagonals
    for k in range(-1, -n, -1):
        diagonal = ""
        for i in range(-k, n):
            if i + k < m:
                diagonal += word_search[i][i + k]
        result.append(diagonal)
    return result

def spin_clockwise(word_search : List[str]) -> List[str]:
    n = len(word_search)
    m = len(word_search[0])
    result = []
    for j in range(m):
        line = ""
        for i in range(n-1,-1,-1):
            line += word_search[i][j]
        result.append(line)
    return result

def arr_to_str(arr : List[str]) -> str:
    return "\n".join(arr)
