#-----Day 25: Running Time and Complexity-------#


import math

def isprime(data):
    x=int(math.ceil(math.sqrt(data)))
    if data==1:
        return "Not prime"
    elif data==2:
        return"Prime"
    else:
        for i in range(2,x+1):
            if data%i==0:
                return "Not prime"
                #break
        else:
            return "Prime"
    return "-1"        
                
s=int(input())
while s:
    d=int(input())
    v=isprime(d) 
    print(v)

              
             






