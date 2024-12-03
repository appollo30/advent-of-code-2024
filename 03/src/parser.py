"""
Module to parse the input file, and output a list of strings which represent the memory.
"""
import os
from typing import Optional, List

def parse(file_name : Optional[str]) -> List[str]:
    """
    Parses the input file

    Args:
        file_name (Optional[str]): Name of the input file

    Returns:
        List[str]: List of strings representing the memory
    """
    file_path = os.path.join(os.getcwd(),"data",file_name)
    if not os.path.exists(file_path):
        print(f"File \"{file_name}\" does not exist")
        return None

    result = []
    with open(file_path,"r",encoding="utf-8") as f:
        lines = f.readlines()
    for l in lines:
        result.append(l)
    return result
