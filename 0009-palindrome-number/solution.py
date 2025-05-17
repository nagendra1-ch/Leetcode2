class Solution:
    def isPalindrome(self, x: int) -> bool:
        n=str(x)
        x=str(x)
        x=x[::-1]
        if x==n:
            return True
        else:
            return False
        
