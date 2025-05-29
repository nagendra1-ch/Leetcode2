class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches=[]
        while n>1:
            if n%2==0:
                n=n//2
                matches.append(n)
            else:
                n=n//2
                matches.append(n)
                n=n+1
        ans=sum(matches)
        return ans

