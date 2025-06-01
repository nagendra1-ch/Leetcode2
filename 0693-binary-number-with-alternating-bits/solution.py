class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        x=n
        bits=''
        while n>0:
            bits+=str(n%2)
            n=n//2
        k,l='',''
        i,j='1','0'
        while x>0:
            k+=i
            l+=j
            i,j=j,i
            x=x//2
        return (k==bits or l==bits)
