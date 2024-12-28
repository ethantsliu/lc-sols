import collections

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        #initially, we can brute force
        #bfs turns out to be a better approach. Either go right or down, run bfs until hits 0
        if not grid:
            return 0

        q = []
        visited = set()

        def bfs(x, y):
            q = collections.deque()
            q.append((x, y))
            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if r in range(len(grid)) and c in range(len(grid[0])) and grid[r][c] == '1' and (r, c) not in visited:
                        q.append((r, c))
                        visited.add((r, c))
            

        count = 0 
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == '1' and (x, y) not in visited: 
                    bfs(x, y)
                    count += 1
        return count