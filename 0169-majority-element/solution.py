class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        n=len(nums)
        freq=1
        max_ele=nums[0]
        for i in range(n):
            if nums[i] in d:
                d[nums[i]]+=1
            else:
                d[nums[i]]=1
        for i in d:
            if d[i]>freq:
                freq=d[i]
                max_ele=i
        return max_ele
