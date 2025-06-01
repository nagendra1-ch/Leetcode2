class Solution:
    def pivotInteger(self, n: int) -> int:
        if n==1:
            return 1
        sum1=0
        sum2=0
        k=0
        x=n
        while n>k:
            sum1=sum(range(1,k+1))
            sum2=sum(range(k,n+1))
            if sum1==sum2:
                return k
            k=k+1
            
        return -1

            

        
