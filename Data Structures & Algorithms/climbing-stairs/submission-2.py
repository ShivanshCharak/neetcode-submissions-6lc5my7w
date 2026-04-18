class Solution:       
    def climbStairs(self, n: int) -> int:
      one = 1
      two = 1
      while n-2 >= 0:
        temp = one 
        one = one + two
        two = temp
        n-=1
      return one
        

