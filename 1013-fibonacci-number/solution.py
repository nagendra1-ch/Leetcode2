class Solution:
    def fib(self, n: int) -> int:
        fib=[0]
        for i in range(1,n+1):
            if i==0 or i==1:
                fib.append(i)
            else:
                fib.append(fib[i-1]+fib[i-2])
        return fib[-1]
        
