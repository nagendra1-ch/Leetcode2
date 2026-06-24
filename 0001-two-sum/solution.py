class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)        
        d={}
        for i in range(n):
            find=target-nums[i]
            if find in d:
                return [i,d[find]]
            d[nums[i]]=i
