class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s=0
        m=1
        while n>0:
            k=n%10
            s=s+k
            m=m*k
            n=n//10
        ans=m-s
        return ans
        
