class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        res = []
        for index , val in enumerate(nums):
            left, right = index+1, len(nums)-1
            if index >0 and nums[index]==nums[index-1]:
                continue
            while left < right:
                total = nums[left]+ nums[right]+nums[index]
                if total < 0:
                    left+=1
                elif total > 0:
                    right-=1
                else:
                    res.append([nums[left], nums[right], nums[index]])
                    while left < right and nums[left]==nums[left+1]:
                        left=left+1
                    while left < right and nums[right]==nums[right-1]:
                        right-=1
                    left+=1
                    right-=1
        return res


