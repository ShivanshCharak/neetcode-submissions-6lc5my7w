class Solution:
    def tribonacci(self, n: int) -> int:
        if  n == 0:
            return n
        t0 = 0
        t1 = 1
        t2 = 1
        for i in range(2,n+1):
            temp = t2
            t2 = t1 + t0 + t2
            t0 = t1
            t1 = temp
        return t1
        