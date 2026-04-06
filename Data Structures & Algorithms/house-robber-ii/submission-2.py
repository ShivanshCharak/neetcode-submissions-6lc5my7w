class Solution:
    def dp(self, nums:List[int], left: int , right:int)->int:
        one, two = nums[left], max(nums[left], nums[left+1])
        print(one,two)
        for i in range(left+2,right+1):
            temp = max(one+nums[i], two)
            one = two
            two = temp
        return two
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        if len(nums) ==2:
            return max(nums[0], nums[1])
        return max(self.dp(nums, 0, len(nums)-2), self.dp(nums,1, len(nums)-1))