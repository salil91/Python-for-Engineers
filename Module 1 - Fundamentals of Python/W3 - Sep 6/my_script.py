# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 14:37:25 2022

@author: salil.bavdekar
"""
from sys import argv

args = argv

if len(argv) < 2:
    name = "User"
else:
    name = argv[1]

print(f"Hello {name}")