class Solution:
    def maxProduct(self, nums: List[int]) -> int:
       currMax, currMin = 1, 1
       ans = float("-inf")
       for n in nums:
            temp = currMax*n
            currMax= max(currMax*n, currMin*n, n)
            currMin = min(temp, currMin*n, n)
            ans = max(currMax,currMin, ans)
       return ans