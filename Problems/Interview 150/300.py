class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        def bs(start, end, target, arr):
            result = -1
            while start <= end:
                mid = (start + end)//2
                if arr[mid] < target:
                    result = mid
                    start = mid+1
                else:
                    end = mid-1

            return result

        result = 0
        stack = []
        for num in nums:
            if len(stack) == 0 or num > stack[len(stack)-1]:
                stack.append(num)
            elif num < stack[0]:
                stack[0] = num
            # if smaller than the largest number, binary search to replace it
            elif num < stack[len(stack)-1]:
                idx = bs(0, len(stack)-1, num, stack)
                stack[idx+1] = num

        return len(stack)

print(Solution().lengthOfLIS([1,2,8,4,5]))
