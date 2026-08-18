from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols=len(grid),len(grid[0])

        queue=deque()

        fresh_count=0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    queue.append((r,c,0))
                if grid[r][c]==1:
                    fresh_count+=1
        if fresh_count==0:
            return 0
        max_minute=0

        while queue:
            r,c,minute=queue.popleft()
            max_minute=max(max_minute,minute)
            for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr,nc=r+dr,c+dc

                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1:
                    grid[nr][nc]=2
                    fresh_count-=1
                    queue.append((nr,nc,minute+1))
        return max_minute if fresh_count==0 else -1