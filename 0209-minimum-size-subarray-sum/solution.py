class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum1=0
        i=0
        if sum(nums)<target:
            return 0
        n=len(nums)
        min_len=n
        for j in range(n):
            sum1+=nums[j]
            while sum1>=target:
                min_len=min(min_len,j-i+1)
                sum1-=nums[i]
                i+=1
        return min_len
