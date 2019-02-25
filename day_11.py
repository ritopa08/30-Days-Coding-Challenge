import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    c=str(bin(n)[2:])
    #print(c)
    count=0
    v=len(c)
    temp=0
    for i in range(v):
        if(c[i]=='1'):
            count+=1
        else:
           count=0
        if(count>temp):    
           temp=count    
    print(temp)         

