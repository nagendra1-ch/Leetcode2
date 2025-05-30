class Solution:
    def numberOfSteps(self, num: int) -> int:
        count=0
        n=num
        while n>0:
            count+=1
            if n%2==0:
                n=n/2
            elif n%2==1:
                n=n-1
            else:
                n=n/2
        return count
        
