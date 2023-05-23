class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        results = []
        if not digits:
            return results
        
        digits_map = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        def backtrack(path, digits_map):
            if len(path) == len(digits):
                results.append(path)
                return
            
            current_digit = digits[len(path)]
            for letter in digits_map[current_digit]:
                backtrack(path+letter, digits_map)

        backtrack("", digits_map)
        return results

print(Solution().letterCombinations('23'))