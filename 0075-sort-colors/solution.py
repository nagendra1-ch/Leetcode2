class Solution:
    def sortColors(self, nums: List[int]) -> None:
        d={}
        for i in range(3):
            d[i]=0
        for i in nums:
                d[i]+=1
            
        nums.clear()
        for k,v in d.items():
            for i in range(v):
                nums.append(k)


