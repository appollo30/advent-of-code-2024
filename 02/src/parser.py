"""
Module to parse the input file, and output a list of integer lists.
"""
import os

def parse(file_name):
    file_path = os.path.join(os.getcwd(),"data",file_name)
    if not os.path.exists(file_path):
        print(f"File \"{file_name}\" does not exist")
        return None

    with open(file_path,"r",encoding="utf-8") as f:
        result = []
        lines = f.readlines()
        for l in lines:
            formated_line = [int(elt) for elt in l.split(" ")]
            result.append(formated_line)
        return result
