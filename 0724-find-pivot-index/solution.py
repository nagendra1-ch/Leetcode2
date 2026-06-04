class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        tsum=sum(nums)
        n=len(nums)
        lsum=0
        rsum=0
        for i in range(n):
            rsum=tsum-lsum-nums[i]
            if lsum==rsum:
                return i
            lsum+=nums[i]
        return -1
