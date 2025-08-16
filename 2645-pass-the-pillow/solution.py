class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        i=1
        direction=1
        while time>0:
            if direction==1:
                i+=1
            if direction==-1:
                i-=1
            if i==n:
                direction=-1
            if i==1:
                direction=1
            time-=1
        return i
