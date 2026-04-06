class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for r in range(2, len(nums)):
            dp[r]=max(dp[r-2] + nums[r], dp[r-1])
        return max(dp[len(nums)-1], dp[len(nums)-2])