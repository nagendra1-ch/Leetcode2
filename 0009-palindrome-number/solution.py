class Solution:
    def isPalindrome(self, x: int) -> bool:
        n=str(x)
        x=n[::-1]
        if x==n:
            return True
        else:
            return False
        
