class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        # for i in range(k):
        # arr=[nums[-1]]
        # arr.extend(nums[0:n-2])
        # nums=[nums[-1]]+nums[:n-2]
        # [nums[-1]]+nums[:n-2]
        arr=[0]*n
        for i in range(n):
            arr[(i+k)%n]=nums[i]
        for i in range(n):
            nums[i]=arr[i]
        

   
