#-----Day 17: More Exceptions-------#


import sys

class Calculator:
    def power(self,n,p):
        if n<0 or p<0:
            raise ValueError("n and p should be non-negative ")
        else:
            return n**p    
    


