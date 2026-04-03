class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set()
        ans = 0
        for n in nums:
            hashset.add(n)
        for i in range(len(nums)):
            longest = 0
            if nums[i]-1 not in hashset:
                val = nums[i]
                while val in hashset:
                    longest+=1
                    val=val+1
                ans = max(longest, ans)
        return ans
             