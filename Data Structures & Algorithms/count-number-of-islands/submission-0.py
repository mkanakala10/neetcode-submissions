from collections import deque

class Solution:


    def numIslands(self, grid: List[List[str]]) -> int:
        def clearIsland(grid, x, y):
            queue = deque([(x, y)])
            while queue:
                i, j = queue.popleft()

                grid[i][j] = "0"

                if i - 1 >= 0 and grid[i - 1][j] == "1" and (i - 1, j) not in visited:
                    queue.append((i - 1, j))
                    visited.add((i - 1, j))
                if i + 1 < len(grid) and grid[i + 1][j] == "1" and (i + 1, j) not in visited:
                    queue.append((i + 1, j))
                    visited.add((i + 1, j))
                if j - 1 >= 0 and grid[i][j - 1] == "1" and (i, j - 1) not in visited:
                    queue.append((i, j - 1))
                    visited.add((i, j - 1))
                if j + 1 < len(grid[0]) and grid[i][j + 1] == "1" and (i, j + 1) not in visited:
                    queue.append((i, j + 1))
                    visited.add((i, j + 1))
        visited = set()
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    res += 1
                    clearIsland(grid, i, j)
        return res


