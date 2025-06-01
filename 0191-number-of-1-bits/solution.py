class Solution:
    def hammingWeight(self, n: int) -> int:
        s=''
        while n>0:
            s+=str(n%2)
            n=n//2
        count=0
        for i in s:
            if i=='1':
                count+=1
        return count
        
