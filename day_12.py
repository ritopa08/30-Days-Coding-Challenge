 #!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    arr = []
    l = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

       

        for i in range(len(arr)-2):
           for j in range(len(arr)-2):
            a = sum(arr[i][j:j+3])
            c = arr[i+1][j+1]
            b = sum(arr[i+2][j:j+3])
            d = a+b+c
            #print(d)
            l.append(d)
            #print(l)
            v=max(l)
    print(v)

