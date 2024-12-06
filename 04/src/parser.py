"""
Module to parse the input file, and output a str representing the lines of the word search.
"""
import os
from typing import Optional

def parse(file_name : Optional[str]) -> str:
    """
    Parses the input file

    Args:
        file_name (Optional[str]): Name of the input file

    Returns:
        str: Str representing the lines of the word search
    """
    file_path = os.path.join(os.getcwd(),"data",file_name)
    if not os.path.exists(file_path):
        print(f"File \"{file_name}\" does not exist")
        return None

    with open(file_path,"r",encoding="utf-8") as f:
        word_search = f.read()
    return word_search.strip()
