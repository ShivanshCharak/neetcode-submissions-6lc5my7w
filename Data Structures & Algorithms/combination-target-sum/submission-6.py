class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.ans = []
        def dfs(i, sum,subset):

            if sum > target or i >= len(nums):
                return
            if sum == target:

                self.ans.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i, sum+nums[i], subset)
            val = subset.pop()
            sum-=val
            dfs(i+1, sum + nums[i], subset)
        dfs(0,0,[])
        return self.ans



    