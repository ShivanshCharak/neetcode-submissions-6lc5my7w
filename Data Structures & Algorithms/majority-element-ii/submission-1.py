class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dic = {}
        res = []
        length = len(nums)
        for n in nums:
            dic[n] = dic.get(n,0)+1
        for val, freq in dic.items():
            if freq > (length/3):
                res.append(val)
        return res

        