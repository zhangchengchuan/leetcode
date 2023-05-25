class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        dp = [False] * (1+len(s))
        dp[0] = True
        cur_str = ""
        for i in range(1, len(s)+1):
            cur_str += s[i-1]
            for word in wordDict:
                if dp[i] == False and cur_str[-len(word):] == word:
                    dp[i] = dp[i-len(word)]
        
        return dp[len(s)]