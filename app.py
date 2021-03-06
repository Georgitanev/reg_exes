# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 10:11:46 2020

@author: G

Please extract all contacts from the text. Valid contacts are like this - #Firstname.Familyname
INPUT:
Welcome to #EMIS. If you need any help from HR you can write to #Milo.Minderbinder. 
For any technical problems you should contact
#Major.Major. If you need any smart advises, please contact #Ali.Baba or #John.Yossarian. 
When you are sick, please stay at #Home.
Please write a program on Perl/Python/JS or your favorite scripting language. 
"""

import re
from typing import Any, List


string = """Welcome to #EMIS. If you need any help from HR you can write to #Milo.Minderbinder. 
For any technical problems you should contact
#Major.Major. If you need any smart advises, please contact #Ali.Baba or #John.Yossarian. 
When you are sick, please stay at #Home."""


string_brasil = """Welcome to #Brasil. Here you can find a lot at #Ore_Sandson.
Your guide name is
#Paolo_Salvini. If you need any smart advises, please contact #Daniel_Paola or #John_Samon.
If it's too hot you can stay at #Home."""


# contacts = re.findall(f'#[A-Z\w.w\t\n]+', string) # original
                      

def dot(contact: str) -> str:
    if contact[-1] == '.':
        contact = contact[:-1]
    return contact


def count_dot(contact: str, deli) -> Any:
    if contact.count(f'{deli}') == None or contact.count(f'{deli}') == False:
        return False
    if contact.count(f'{deli}') == 1:
        return contact


def regex_parser(string: str, deli: str = '.') -> List:
    contacts = re.findall(f'#[A-Z\w{deli}w\t\n]+', string)
    list1 = []
    for contact in contacts:
        contact = dot(contact)
        if count_dot(contact, deli) == None or count_dot(contact, deli) == False:
            pass
        else:
            list1.append(count_dot(contact, deli))
    return list1


print(regex_parser(string=string, deli='.'))
print(regex_parser(string=string_brasil, deli='_'))


