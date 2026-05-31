class Solution:
    def isHappy(self, n: int) -> bool:
        s=set()
        while n>1:
            if n not in s:
                s.add(n)
                k=0
                while n>0:
                    x=n%10
                    k+=x*x
                    n//=10
                n=k
                
            else:
                return False
        return n==1
