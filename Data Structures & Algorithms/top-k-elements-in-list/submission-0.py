class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        freq = [[] for i in range(len(nums)+1)]
        for num in nums:
            dic[num]=dic.get(num,0)+1
        for numb, index in dic.items():
            freq[index].append(numb)
        res = []
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res)==k:
                    return res

        
        