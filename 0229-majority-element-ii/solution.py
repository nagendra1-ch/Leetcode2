class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        r=[]
        for i in d:
            if d[i]>n//3:
                r.append(i)
        return r
