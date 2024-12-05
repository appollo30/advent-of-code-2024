"""
Module to parse the input file, and output a list of integer lists.
"""
import os
from typing import List, Optional

def parse(file_name : Optional[str]) -> Optional[List[List[int]]]:
    """
    Parses the input file

    Args:
        file_name (Optional[str]): The name of the input file

    Returns:
        Optional[List[List[int]]]: None, or the list of reports
    """
    file_path = os.path.join(os.getcwd(),"data",file_name)
    if not os.path.exists(file_path):
        print(f"File \"{file_name}\" does not exist")
        return None

    result = []
    with open(file_path,"r",encoding="utf-8") as f:
        lines = f.readlines()

    for l in lines:
        formated_line = [int(elt) for elt in l.split(" ")]
        result.append(formated_line)
    return result
