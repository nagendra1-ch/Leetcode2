from collections import Counter
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        c=Counter(nums)
        s=0
        for i in c:
            if c[i]==1:
                s+=i
        return s
