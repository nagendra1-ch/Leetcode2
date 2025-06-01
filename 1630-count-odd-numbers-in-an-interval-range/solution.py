class Solution:
    def countOdds(self, low: int, high: int) -> int:
        count=0
        if low%2==0:
            count=len(range(low+1,high+1,2))
        else:
            count=len(range(low,high+1,2))

        return count
