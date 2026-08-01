class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        def dfs(i: int, sum: int):
            if sum > target or i >= len(nums):
                return 
            if sum == target:
                res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i, sum+nums[i])
            subset.pop()
            dfs(i+1, sum)
        dfs(0, 0)
        return res
        