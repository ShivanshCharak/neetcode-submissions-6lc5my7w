class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visit = set()
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==0:
                    q.append((i,j))
                    visit.add((i,j))
                    print(q,visit)
        def bfs(i, j):
            if i < 0 or j < 0 or i >= ROWS or j >= COLS or grid[i][j]==-1 or (i,j) in visit:
                return
            q.append((i,j))
            visit.add((i,j))
        dist = 0
        while q:
            for i in range(len(q)):
                r, c= q.popleft()
                print(r,c)
                grid[r][c] = dist
                bfs(r+1,c)
                bfs(r,c+1)
                bfs(r-1,c)
                bfs(r, c-1)
            dist+=1

                
            