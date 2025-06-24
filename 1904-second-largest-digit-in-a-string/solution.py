class Solution:
    def secondHighest(self, s: str) -> int:
        s1=''
        new=['1','2','3','4','5','6','7','8','9','0']
        for i in s:
            for j in new:
                if j==i:
                    s1+=i+' '
                    break
        l=list(map(int,s1.split()))
        max1=-1
        secondMax=-1
        for i in range(len(l)):
            if max1<l[i]:
                secondMax=max1
                max1=l[i]
            if l[i]>secondMax and l[i]!=max1:
                secondMax=l[i]
        return secondMax
