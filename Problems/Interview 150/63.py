class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        if obstacleGrid[len(obstacleGrid)-1][len(obstacleGrid[0])-1] == 1 or obstacleGrid[0][0] == 1: return 0
        # dp = [[0 for i in range(len(obstacleGrid[0]))] for j in range(len(obstacleGrid))]
        dp = [0 for i in range(len(obstacleGrid[0]))]
        temp_dp = [0 for i in range(len(obstacleGrid[0]))]
        temp_dp[0] = 1
        for r in range(len(obstacleGrid)):
            for c in range(len(obstacleGrid[0])):
                if obstacleGrid[r][c]: continue
                
                if not r and not c: continue
                
                temp_dp[c] = (temp_dp[c-1] if c>0 else 0) + (dp[c] if r>0 else 0)
            dp = temp_dp
            temp_dp = [0 for i in range(len(obstacleGrid[0]))]

        return temp_dp[len(obstacleGrid[0])-1]

print(Solution().uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))