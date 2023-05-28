# class Solution:
#     def maximalSquare(self, matrix: list[list[str]]) -> int:
#         max_len=0
#         for i in range(1, min(len(matrix), len(matrix[0]))+1):
#             looping = False
#             # each iteration, search 1 less row
#             for r in range(len(matrix)-i+1):
#                 for c in range(len(matrix[0])-i+1):
#                     if matrix[r][c] == '0': continue
                    
#                     # Just need to confirm that there is at least a '1'
#                     if i==1:
#                         looping = True
#                         break

#                     # CHECK RIGHT, DOWN, DOWNRIGHT
#                     if not (matrix[r][c+1]=='1' and matrix[r+1][c]=='1' and matrix[r+1][c+1]=='1'):
#                         matrix[r][c] = '0'
#                     else:
#                         looping = True

#             # There were no squares of "i" length
#             if not looping:
#                 break
#             else:
#                 max_len = i

#         return max_len**2

import sys
class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        dp = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        max_len = 0
        for r in range(len(matrix)-1, -1, -1):
            for c in range(len(matrix[0])-1, -1, -1):
                if matrix[r][c] == '0': continue

                dp[r][c] = min(dp[r][c+1] if c+1<len(matrix[0]) else 0, 
                               dp[r+1][c] if r+1<len(matrix) else 0, 
                               dp[r+1][c+1] if (c+1<len(matrix[0]) and r+1<len(matrix)) else 0) + 1
                
                max_len = max(max_len, dp[r][c])
        
        return max_len**2

                


print(Solution().maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))