class Solution:
    def countDigits(self, num: int) -> int:
        count=0
        x=str(num)
        for i in x:
            if num%int(i)==0:
                count+=1
        return count
        
