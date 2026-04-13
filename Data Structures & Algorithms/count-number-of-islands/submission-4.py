class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        island=0
        directions =[[1,0],[0,1],[-1,0],[0,-1]]
        def dfs(i,j):
            if i < 0 or j <0 or i >= ROWS or j >= COLS or grid[i][j]=="0":
                return 
            grid[i][j]="0"
            dfs(i+1,j)
            dfs(i,j+1)
            dfs(i-1,j)
            dfs(i,j-1)
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]=="1":
                    dfs(i,j)
                    island+=1
        return island