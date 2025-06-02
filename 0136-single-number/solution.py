class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        frequency=[0]*1000000
        for i in nums:
            frequency[i]+=1
        for i in nums:
            if frequency[i]==1:
                return i
