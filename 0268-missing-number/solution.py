class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        max=nums[0]
        nums.sort()
        for i in range(len(nums)):
            if max<nums[i]:
                max=nums[i]
        for i in range(0,max+1):
            if i == nums[i]:
                continue
            else:
                return i
        return i+1
