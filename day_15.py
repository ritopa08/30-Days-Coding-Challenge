
l=[]
t=len(a)
# Add your code here
for i in range(t):
    for j in range(i+1,t):
        
        l.append(abs(a[i]-a[j]))
        #print(l)
        g=max(l) 
               
               
               
print(g) 
return 0
            


