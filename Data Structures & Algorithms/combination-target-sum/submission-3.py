class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        subset  = []
        res  = []
        def dfs(subset,i,sum):

            if sum == target:
                res.append(subset.copy())
                return
            
            if sum > target or i >= len(nums):
                return
            subset.append(nums[i])
            dfs(subset, i, sum+nums[i])
            sum-=subset.pop()
            
            dfs(subset, i+1, sum+nums[i])
        dfs(subset, 0, 0)
        return res