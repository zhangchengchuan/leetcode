class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        count = 0
        d = {}
        for i in range(len(grid[0])):
            x = ",".join([str(grid[x][i]) for x in range(len(grid))])
            if x not in d:
                d[x] = 0
            d[x] += 1
        
        for r in range(len(grid)):
            x = ",".join([str(x) for x in grid[r]])
            if x in d:
                count += d[x]

        return count
print(Solution().equalPairs([[11,1],[1,11]]))