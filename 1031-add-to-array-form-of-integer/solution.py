class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        s=0
        for i in num:
            s=s*10+i
        s+=k
        num=[]
        while s:
            num.append(s%10)
            s//=10
        return num[::-1]
