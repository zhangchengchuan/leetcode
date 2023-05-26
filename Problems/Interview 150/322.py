import sys

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [-1] * (1+amount)
        dp[0] = 0
        for i in range(1, amount+1):
            minimum = sys.maxsize
            for coin in coins:
                if coin > i: continue

                if dp[i-coin] != -1:
                    minimum = min(minimum, dp[i-coin]+1)

        return dp[amount]
