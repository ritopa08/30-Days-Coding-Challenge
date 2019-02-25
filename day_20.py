#-----Day 19: Interfaces-------#


class Calculator(AdvancedArithmetic):
     def divisorSum(self, n):
        l=[]
        
        for i in range (1,n+1):
            if n%i==0:
                l.append(i)
            else:
                 pass
                
        return sum(l)




