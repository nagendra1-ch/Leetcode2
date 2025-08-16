class Solution:
    def largestGoodInteger(self, num: str) -> str:
        s=set(num)
        l=[]
        for i in s:
            if i*3 in num:
                l.append(i*3)
        if l:
            return max(l)
        return ""
