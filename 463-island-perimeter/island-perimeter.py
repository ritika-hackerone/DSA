class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0 #perimeter
        for r in range(m):
            for c in range(n):
                if grid[r][c]==1:   # land cell
                    ans+=4          # Start with 4 sides for this land cell

                    # Check top neighbor
                    # If the cell above is also land, two sides (one from current, one from top) are shared, so subtract 2
                    if r > 0 and grid[r-1][c] == 1:
                        ans-=2
                    # Check left neighbor
                    # If the cell to the left is also land, two sides are shared, so subtract 2
                    if c > 0 and grid[r][c-1] == 1:
                        ans-=2
        return ans
        