class Solution:
    def maxAreaOfIsland(self, arr: List[List[int]]) -> int:
        rows, cols = len(arr), len(arr[0])
        visited = set()
        maxArea= 0
        def dfs(i, j , island):
            if i < 0 or j < 0 or i >= rows or j >= cols or (i,j) in visited or arr[i][j]==0:
                return
            island.add((i,j))
            visited.add((i,j))
            dfs(i+1,j,island)
            dfs(i,j+1,island)
            dfs(i-1,j,island)
            dfs(i,j-1,island)
            return len(island)
        for i in range(rows):
            for j in range(cols):
                if arr[i][j] == 1 and (i,j) not in visited:
                    island = set()
                    maxArea = max(maxArea,dfs(i,j, island))
        return maxArea

        
        