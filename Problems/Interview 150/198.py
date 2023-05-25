class Solution:
    def rob(self, nums: list[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        
        max_prof = dp[0]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
            max_prof = max(max_prof, dp[i])
        
        return max_prof

print(Solution().rob([2,7,9,3,1]))
