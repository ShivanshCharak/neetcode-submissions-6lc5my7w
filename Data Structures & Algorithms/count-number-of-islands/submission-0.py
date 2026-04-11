class Solution:
    def numIslands(self, arr: List[List[str]]) -> int:
        islands = set()
        sum = 0
        row, cols = len(arr), len(arr[0])
        def dfs(i,j):
            if i<0 or j<0 or i >=row or j >=cols or (i,j) in islands or arr[i][j]=="0": 
                return 
            islands.add((i,j))
            dfs(i+1,j)
            dfs(i, j+1)
            dfs(i-1,j)
            dfs(i,j-1)
        for i in range(row):
            for j in range(cols):
                if arr[i][j]=="1" and (i,j) not in islands:
                        dfs(i,j)
                        sum+=1
                        
        return sum
        