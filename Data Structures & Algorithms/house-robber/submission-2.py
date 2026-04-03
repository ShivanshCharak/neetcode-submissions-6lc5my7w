class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        ans = [0]*len(nums)
        ans[0], ans[1]  = nums[0], max(nums[0], nums[1])
        for n in range(2, len(nums)):
            ans[n] = max(ans[n-2] + nums[n], ans[n-1])
        return ans[-1]