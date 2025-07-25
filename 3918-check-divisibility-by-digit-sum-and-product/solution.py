class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s=0
        p=1
        n1=n
        while n>0:
            r=n%10
            s+=r
            p*=r
            n//=10
        return n1%(s+p)==0
