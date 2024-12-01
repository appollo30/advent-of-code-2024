"""
Module to parse the input file, and output two integer lists.
"""
import os
from typing import List, Tuple, Optional

def parse(file_name : Optional[str]) -> Optional[Tuple[List[int]]]:
    """
    Parses the input file
    
    Args:
        file_name (Optional[str]): The name of he input file.

    Returns:
        Optional[Tuple[List[int]]]: None, or a tuple of shape (list1,list2) which are integer lists.
    """
    file_path = os.path.join(os.getcwd(),"data",file_name)
    if not os.path.exists(file_path):
        print(f"File \"{file_name}\" does not exist")
        return None
    
    with open(file_path,"r",encoding="utf-8") as f:
        list1 = []
        list2 = []
        line = f.readline()
        while line:
            split_text = line.split("   ")
            list1.append(int(split_text[0]))
            list2.append(int(split_text[1]))
            line = f.readline()
    return list1,list2
