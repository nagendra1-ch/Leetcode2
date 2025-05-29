class Solution:
    def addDigits(self, num: int) -> int:
        while num>9:
            num1=str(num)
            add=0
            for i in num1:
                add=add+int(i)
            num=add

        return num
        
