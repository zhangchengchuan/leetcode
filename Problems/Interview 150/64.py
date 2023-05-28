import sys
class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        dp = [[sys.maxsize for i in range(len(grid[0]))] for j in range(len(grid))]
        dp[0][0] = grid[0][0]
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if r==0 and c==0: continue
                dp[r][c] = grid[r][c] + min(dp[r][c-1] if c>0 else sys.maxsize, dp[r-1][c] if r>0 else sys.maxsize)

        return dp[len(grid)-1][len(grid[0])-1]

print(Solution().minPathSum([[1,3,1],[1,5,1],[4,2,1]]))