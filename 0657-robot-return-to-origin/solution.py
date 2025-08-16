class Solution:
    def judgeCircle(self, moves: str) -> bool:
        u,l,d,r=0,0,0,0
        for i in moves:
            if i=='U':
                u+=1
            elif i=='D':
                d+=1
            elif i=='L':
                l+=1
            else:
                r+=1
        return r==l and u==d
