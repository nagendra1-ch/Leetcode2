class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counter=Counter(arr)
        ans=-1
        for item in counter:
            if item==counter[item]:
                if item>ans:
                    ans=item
        return ans
