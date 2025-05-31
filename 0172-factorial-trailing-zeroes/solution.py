import math
import sys
sys.set_int_max_str_digits(1000000)
class Solution:
    def trailingZeroes(self, n: int) -> int:
        fact=str(math.factorial(n))
        count=0
        fact=str(fact)
        i=-1
        while fact[i]=='0':
            count+=1
            i-=1
        return count
