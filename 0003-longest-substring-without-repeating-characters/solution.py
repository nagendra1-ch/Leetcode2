class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        ml=0
        s1=set()
        n=len(s)
        for r in range(n):
            while s[r] in s1:
                s1.remove(s[l])
                l+=1
            w=(r-l)+1
            ml=max(w,ml)
            s1.add(s[r])
        return ml
