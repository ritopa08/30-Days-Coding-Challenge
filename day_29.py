#-----Day 28: RegEx, Patterns, and Intro to Databases-------#



#!/bin/python3

import math
import os
import random
import re
import sys


N = int(input().strip())
l = []

for i in range(N):
    f, eId = input().strip().split(' ')
    #print(type(f),f)
    #print(type(eId),eId)
    if re.search("@gmail.com",eId):
        l.append(f)
#print(l) 
'''k=sorted(l)
   for i in k:
    print(i)
'''
print(*sorted(l), sep='\n')
