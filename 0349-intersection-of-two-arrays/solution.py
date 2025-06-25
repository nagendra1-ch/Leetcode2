class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result=[]
        nums1.sort()
        nums2.sort()
        x,y=0,0
        l1,l2=len(nums1),len(nums2)
        while x<l1 and y<l2:
            if nums1[x]==nums2[y]:
                result.append(nums1[x])
                x+=1
                y+=1
            elif nums1[x]<nums2[y]:
                x+=1
            elif nums1[x]>nums2[y]:
                y+=1
        result=list(set(result))
        return result
