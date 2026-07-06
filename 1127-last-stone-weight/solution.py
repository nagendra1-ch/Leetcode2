class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n=len(stones)
        for i in range(n):
            stones[i]=-stones[i]
        heapq.heapify(stones)
        while n>1:
            largest=heapq.heappop(stones)
            next_largest=heapq.heappop(stones)
            n-=2
            if largest!=next_largest:
                heapq.heappush(stones,largest-next_largest)
                n+=1
        return -heapq.heappop(stones) if stones else 0
