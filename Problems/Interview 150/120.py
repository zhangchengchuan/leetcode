import sys
class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        dp = [sys.maxsize for i in range(len(triangle[-1]))]
        dp[0] = triangle[0][0]
        for i in range(1, len(triangle)):
            temp_dp = [sys.maxsize for i in range(len(triangle[-1]))]
            for j in range(0, i+1):
                temp_dp[j] = triangle[i][j] + min(dp[j], dp[j-1] if j > 0 else sys.maxsize)
            dp = temp_dp

        return min(dp)
