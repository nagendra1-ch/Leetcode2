class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ws=0
        n=len(nums)
        for i in range(k):
            ws+=nums[i]
        maximum=ws
        for i in range(k,n):
            ws=ws+nums[i]-nums[i-k]
            maximum=max(maximum,ws)
        return maximum/k
