class Solution:
    def maxDepth(self, s: str) -> int:
        c=0
        maxcount=0
        st=[]
        for ch in s:
            if ch=='(':
                c+=1
                st.append('(')
            elif ch==')':
                maxcount=max(c,maxcount)
                c-=1
                st.pop()
            
        return maxcount
