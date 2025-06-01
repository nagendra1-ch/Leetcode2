class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        add_l=sum(nums)
        s=''
        for i in nums:
            s+=str(i)
        add_d=0
        for i in s:
            add_d+=int(i)
        return add_l-add_d
