"""
Module to parse the input file, and output **
"""
import os
from typing import Optional, List

def parse(file_name : Optional[str]) -> List[str]:
    file_path = os.path.join(os.getcwd(),"data",file_name)
    if not os.path.exists(file_path):
        print(f"File \"{file_name}\" does not exist")
        return None

    with open(file_path,"r",encoding="utf-8") as f:
        word_search = f.read()
    return word_search.splitlines()
