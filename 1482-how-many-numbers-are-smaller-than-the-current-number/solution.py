class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        d={}
        for i,v in enumerate(sorted(nums)):
            if v not in d:
                d[v]=i
        ans=[d[v] for v in nums]
        return ans
