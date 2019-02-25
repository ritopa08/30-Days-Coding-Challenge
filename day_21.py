#-----Day 20: Sorting-------#



import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
m=len(a)
c=0
# Write Your Code Here
for i in range (n):
  
    for j in range(1,m):
        if(a[j-1]>a[j]):
            c=c+1
            a[j-1],a[j]=a[j],a[j-1]
            
print("Array is sorted in",c,"swaps.")
print("First Element:",a[0])
print("Last Element:",a[m-1])





