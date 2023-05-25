class Solution:
    def climbStairs(self, n: int) -> int:
        a = 1
        b = 2
        for i in range(2, n):
            a, b = b, a+b
        
        return b

print(Solution().climbStairs(4))