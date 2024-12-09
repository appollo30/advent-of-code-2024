"""
Module to parse the input file, and output **
"""
import os
from typing import Optional

def parse(file_name : Optional[str]):
    file_path = os.path.join(os.getcwd(),"data",file_name)
    if not os.path.exists(file_path):
        print(f"File \"{file_name}\" does not exist")
        return None

    with open(file_path,"r",encoding="utf-8") as f:
        file_content = f.read()
    return file_content
