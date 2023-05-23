class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row, cols, diag, antidiag):
            if row == n-1:
                return 1
            
            solutions = 0
            for col in range(n):
                diagonal = row-col
                antidiagonal = row+col

                if col in cols or diagonal in diag or antidiagonal in antidiag:
                    continue
            
                diag.add(diagonal)
                antidiag.add(antidiagonal)
                cols.add(col)

                solutions += backtrack(row+1, cols, diag, antidiag)

                diag.remove(diagonal)
                antidiag.remove(antidiagonal)
                cols.remove(col)
            
            return solutions

        return backtrack(0, set(), set(), set())