class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # frequency=[0]*1000000
        # for i in nums:
        #     frequency[i]+=1
        # for i in nums:
        #     if frequency[i]==1:
        # #         return i
        # dic={}
        # for i in nums:
        #     if i in dic:
        #         dic[i]+=1
        #     else:
        #         dic[i]=1
        # for i in dic:
        #     if dic[i]==1:
        #         return i
        n=len(nums)
        single=nums[0]
        for i in range(n-1):
            single=single^nums[i+1]
        return single
