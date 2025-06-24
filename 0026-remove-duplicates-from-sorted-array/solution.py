class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index=1
        list=nums
        for i in range(1,len(list)):
            if list[i-1]!=list[i]:
                list[index]=list[i]
                index+=1
        return index
                        
