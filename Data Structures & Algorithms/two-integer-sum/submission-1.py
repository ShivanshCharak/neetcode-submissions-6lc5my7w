class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for index, val in enumerate(nums):
            remaining =  target-val
            print(remaining, dic)
            if remaining in dic:
                return [dic[remaining], index, ]
            dic[val]=index
         
        