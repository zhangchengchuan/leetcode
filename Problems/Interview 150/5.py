class Solution:
    def longestPalindrome(self, s: str) -> str:
        final_R = final_L = 0
        for idx, char in enumerate(s):
            L = R = idx
            while L >= 0 and R < len(s):
                if s[L] == s[R]:
                    if R-L+1 > final_R-final_L+1:
                        final_R = R
                        final_L = L
                    L-=1
                    R+=1
                else:
                    break
            L = R = idx
            R += 1
            while L >= 0 and R < len(s):
                if s[L] == s[R]:
                    if R-L+1 > final_R-final_L+1:
                        final_R = R
                        final_L = L
                    L-=1
                    R+=1
                else:
                    break

        return s[final_L:final_R+1]

print(Solution().longestPalindrome("babad"))