class Solution:
  def new21Game(self, N: int, K: int,W: int) -> float:
     
    if K == 0 or N >= K - 1 + W:
        return 1.0

    dp = [0.0] * (N + 1)
    dp[0] = 1.0
    windowSum = 1.0
    ans = 0.0

    for i in range(1, N + 1):
        dp[i] = windowSum / W
        if i < K:
            windowSum += dp[i]
        else:
            ans += dp[i]
        if i - W >= 0:
            windowSum -= dp[i - W]

    return ans

