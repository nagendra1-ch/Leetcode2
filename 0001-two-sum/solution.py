class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        x,y=0,n-1
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if nums[i]+nums[j]==target:
                    # return [i,j]
        # while x<y:
        #     if nums[x]+nums[y]==target:
        #         return [x,y]
        #     elif nums[x]+nums[y]>target:
        #         y-=1
        #     else:
        #         x+=1
        
        # return -1
        d={}
        for i in range(n):
            find=target-nums[i]
            if find in d:
                return [i,d[find]]
            d[nums[i]]=i
