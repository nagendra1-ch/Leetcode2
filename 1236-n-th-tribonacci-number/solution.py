class Solution:
    def tribonacci(self, n: int) -> int:
        tri=[]
        for i in range(n+1):
            if i==0 :
                tri.append(i)
            elif i==1 or i==2:
                tri.append(1)
            else:
                tri.append(tri[i-1]+tri[i-2]+tri[i-3])
        return tri[-1]
        
