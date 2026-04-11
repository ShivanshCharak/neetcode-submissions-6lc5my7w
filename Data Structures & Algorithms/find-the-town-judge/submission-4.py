class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        judge=trust[0][1]
        for t in trust:
            if t[0]==t[1] or t[0] == judge or t[1] != judge:
                return -1
        return judge        
        