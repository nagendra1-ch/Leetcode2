class Solution:
    def averageValue(self, nums: List[int]) -> int:
        sum=0
        count=0
        for i in nums:
            if i%3==0 and i%2==0:
                sum+=i
                count+=1
        return sum//count if count!=0 else 0
