class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        e=[]
        o=[]
        for i in nums:
            if i%2:
                o.append(i)
            else:
                e.append(i)
        return e+o
