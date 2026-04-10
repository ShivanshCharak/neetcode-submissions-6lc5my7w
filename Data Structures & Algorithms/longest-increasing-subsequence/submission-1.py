from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp =[nums[0]]
        counter = 1
        for i in range(1,len(nums)):
            if dp[-1] < nums[i]:
                dp.append(nums[i])
                counter+=1
                continue
            idx = bisect_left(dp,nums[i])
            dp[idx]=nums[i]
        return counter
            
        