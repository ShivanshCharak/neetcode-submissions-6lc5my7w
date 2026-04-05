class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numb  = set()
        for n in nums:
            if n in numb:
                return True
            numb.add(n)
        return False