class Solution:
    def findMedianSortedArrays(self, a: List[int], b: List[int]) -> float:
        l=[]
        m,n=len(a),len(b)
        x,y=0,0
        while x!=m and y!=n:
            if a[x]>=b[y]:
                l.append(b[y])
                y+=1
            elif a[x]<b[y]:
                l.append(a[x])
                x+=1
        if x<m:
            for i in range (x,m):
                l.append(a[i])
        if y<n:
            for i in range(y,n):
                l.append(b[i])
        n=len(l)
        if n%2==1:
            return l[n//2]
        else:
            return (l[n//2-1]+l[n//2])/2

        
