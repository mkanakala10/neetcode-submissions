from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:


        from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: list[list[int]]) -> None:
        queue = deque()
        visited = set()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append((i, j, 0)) 
                    visited.add((i, j))
                    
        while queue:
            i, j, distance = queue.popleft()
            
            neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
            
            for m, n in neighbors:
                if -1 < m < len(grid) and -1 < n < len(grid[0]):
                    
                    if grid[m][n] == 2147483647 and (m, n) not in visited:
                        visited.add((m, n))
                        
                        grid[m][n] = distance + 1
                        
                        queue.append((m, n, distance + 1))