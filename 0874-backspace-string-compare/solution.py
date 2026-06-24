class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        l=[]
        for i in s:
            if i=='#' and l:
                l.pop()
            elif i!='#':
                l.append(i)
        l1=[]
        for i in t:
            if i=='#' and l1:
                l1.pop()
            elif i!='#':
                l1.append(i)
        return l==l1
