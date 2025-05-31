class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        n=str(x)
        ans=0
        for i in n:
            ans+=int(i)
        if x%ans==0:
            return ans
        else:
            return -1
        
