class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        result = 0
        n, m = len(grid), len(grid[0])
        
        for x in range(n):
            for y in range(m):
                
                if grid[x][y] == 1:
                    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        nx, ny = x + dx, y + dy

                        if nx < 0 or nx >= n or ny < 0 or ny >= m or grid[nx][ny] == 0:
                            result += 1
        
        return result