"""
Module to parse the input file, and output two formatted outputs :
  - One dictionnary that takes integers as keys and outputs sets of integers.
  - One List of integer lists
  
The dictionnary rperesents rules and the list of lists represents the updates
"""
import os
from collections import defaultdict
from typing import Optional, Dict, Set, List, Tuple

def format_rules(rules_str : str) -> Dict[int,Set[int]]:
    """
    Format the rules string into a dictionnary
    The dictionnary takes integers as keys and outputs sets of integers
    The dictionnary represents rules

    Args:
        rules_str (str): String that represents the rules

    Returns:
        Dict[int,Set[int]]: Dictionnary that represents the rules
    """
    rules_dict = defaultdict(set)
    rules_split = rules_str.splitlines()
    for rule in rules_split:
        rule_split = rule.split("|")
        before, after = int(rule_split[0]), int(rule_split[1])
        rules_dict[before].add(after)
    return rules_dict

def format_updates(updates_str : str) -> List[List[int]]:
    """
    Format the updates string into a list of lists
    The list of lists represents the updates
    
    Args:
        updates_str (str): String that represents the updates
    
    Returns:
        List[List[int]]: List of the updates
    """
    updates_list = []
    updates_split = updates_str.splitlines()
    for update in updates_split:
        updates_list.append([int(page) for page in update.split(',')])
    return updates_list

def parse(file_name : Optional[str]) -> Optional[Tuple[Dict[int,Set[int]],List[List[int]]]]:
    """
    Parse the input file and output two formatted outputs :
    - One dictionnary that takes integers as keys and outputs sets of integers.
    - One List of integer lists

    Args:
        file_name (Optional[str]): String that represents the file name

    Returns:
        Optional[Tuple[Dict[int,Set[int]],List[List[int]]]]: Tuple that contains the rules 
        dictionnary and the updates list
    """
    file_path = os.path.join(os.getcwd(),"data",file_name)
    if not os.path.exists(file_path):
        print(f"File \"{file_name}\" does not exist")
        return None, None

    with open(file_path,"r",encoding="utf-8") as f:
        file_content = f.read()
    content_split = file_content.split('\n\n')
    rules_str = content_split[0]
    updates_str = content_split[1]
    rules_dict = format_rules(rules_str)
    updates_list = format_updates(updates_str)
    return rules_dict,updates_list
