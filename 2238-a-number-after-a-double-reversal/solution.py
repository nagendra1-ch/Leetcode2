class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        num1=str(num)
        num1=num1[::-1]
        num1=int(num1)
        num1=str(num1)
        num1=num1[::-1]
        num1=int(num1)
        if num1==num:
            return True
        else:
            return False
        
