class Solution(object):
    def shortestBridge(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        from collections import deque

        def dfs(grid, visited, queue, curr, directions):
            i, j = curr
            if (i, j) in visited:
                return
            visited.add((i, j))
            queue.append((i, j))
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] == 1:
                    dfs(grid, visited, queue, (ni, nj), directions)
        n = len(grid)
        visited = set()
        found_first = False
        queue = deque()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # identify first island and mark as visited
        for i in range(n):
            if found_first:
                break
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(grid, visited, queue, (i, j), directions)
                    found_first = True
                    break

        # BFS to find shortest path to second island
        steps = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                i, j = queue.popleft()
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < n and (ni, nj) not in visited:
                        if grid[ni][nj] == 0:
                            queue.append((ni, nj))
                        else:
                            return steps
                        visited.add((ni, nj))
            steps += 1

        return -1 # if second island not found, return -1

