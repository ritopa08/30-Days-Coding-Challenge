import string


n=int(input())
l=[]
l1=[]
while(n):
    
    m=input()
    for i in range(len(m)):
      if i%2!=0:
          l.append(m[i])
      else:
          l1.append(m[i])
        
    x=''.join(l1)
    y=''.join(l)
    print (x+ " " +y)
    x=None
    y=None
    l1=[]
    l=[]
   
      
n=n-1
