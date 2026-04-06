class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one = cost[len(cost)-2]
        two = cost[len(cost)-1]
        for i in range(len(cost)-3,-1,-1):
            temp = one
            one = min(one, two)+cost[i]
            two = temp
            print(one,two)
        return min(one,two)
            
        