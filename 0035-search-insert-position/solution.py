class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n=len(nums)
        def search(nums,i,j,t):
            if i>j:
                return i
            mid=(i+j)//2
            if nums[mid]==t:
                return mid
            elif nums[mid]>target:
                return search(nums,i,mid-1,t)
            else:
                return search(nums,mid+1,j,t)
        return search(nums,0,n-1,target)
        
