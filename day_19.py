#-----Day 18: Queues and Stacks-------#




class Solution:
    # Write your code here
    def __init__(self):
        self.a=[]
        self.b=[]
    def pushCharacter(self,ch):
        self.a.append(ch)
        
    def popCharacter(self):
        return self.a.pop()
        
    def enqueueCharacter(self,ch):
        self.b.insert(0,ch)
        
    def dequeueCharacter(self):    
        return self.b.pop()




