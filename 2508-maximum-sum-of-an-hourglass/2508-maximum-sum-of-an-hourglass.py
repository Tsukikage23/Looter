class Solution(object):
    def maxSum(self, grid):
        sum1 = 0
        maxsum = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m-2):
            for j in range(n-2):
                sum1 = grid[i][j]+grid[i][j+1]+grid[i][j+2]+grid[i+1][j+1]+grid[i+2][j]+grid[i+2][j+1]+grid[i+2][j+2]
                maxsum = max(maxsum,sum1)
        return maxsum