
from collections import deque
from typing import List


class Solution:
    
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        row = len(grid)
        col = len(grid[0])
        
        if grid[0][0] == 1 or grid[row - 1][col - 1] == 1:
            return -1
        
        if row == 1 and col == 1:
            return 1
        
        q = deque()
        q.append((0,0))
        # matrix is just grid[0][0] not grid[0, 0]
        #grid[0, 0] = -1
        
        grid[0][0] = -1
        
        path = 1
        
        dirR = [ -1, 1, 0, 0, -1, -1, 1, 1 ]
        dirC = [ 0, 0, -1, 1, -1, 1, -1, 1 ]
        
        while q:
            level = len(q)
            
            for i in range(level):
                (r, c) = q.popleft()
                grid[r, c] = -1
                
                for k in range(8):
                    kr = dirR[k] + r
                    kc = dirC[k] + c
                    
                    if kr < 0 or kc < 0 or kr >= row or kc >= col:
                        continue
                    
                    if grid[kr][kc] != 0:
                        continue
                    
                    if kr == row - 1 and kc == col - 1:
                        return path + 1
                    
                    q.append((kr, kc))
                    grid[kr][kc] = -1
            
            path += 1
        
        return -1
    
    def numIslands(self, grid: List[List[str]]) -> int:
        row =  len(grid)
        col = len(grid[0])
        
        island = 0
        q = deque()
        
        # mistake initializing the boolean array
        # visited = List[list[bool]]
        
        visited = [[False] * col for _ in range(row)]
        
        dirR = [1, -1, 0, 0]
        dirC = [0, 0, 1, -1]
        
        for r in range(row):
            for c in range(col):
                
                if grid[r][c] == "1" and visited[r][c] == False:
                    q.append((r, c))
                    visited[r][c] = True
                
                    while q:
                        
                        (rr, cc) = q.popleft()
                        
                        for k in range(4):
                            kr = dirR[k] + rr
                            kc = dirC[k] + cc
                            
                            if kr < 0 or kc < 0 or kr >= row or kc >= col:
                                continue
                            
                            if visited[kr][kc] == True or grid[kr][kc] == "0":
                                continue
                            
                            q.append((kr, kc))
                            visited[kr][kc] = True
                    
                    island += 1
        
        return island
    
    
if __name__ == "__main__":
    sol = Solution()
    res = sol.shortestPathBinaryMatrix()
    print(res)