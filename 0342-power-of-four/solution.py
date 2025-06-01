class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        r=0
        while n>0:
            r+=n%4
            n=n//4
        return r==1
