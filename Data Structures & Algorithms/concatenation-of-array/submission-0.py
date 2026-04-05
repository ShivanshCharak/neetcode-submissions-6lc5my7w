class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        left = 0
        right =  len(nums)
        ans = [0]*(len(nums)*2)
        while left < len(nums):
            ans[left] =  ans[right] = nums[left]
            left+=1
            right+=1
        return ans
        