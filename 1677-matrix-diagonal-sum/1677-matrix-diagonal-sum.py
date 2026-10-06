class Solution(object):
    def diagonalSum(self, mat):
        r = len(mat)
        sum1 = 0
        for i in range(r):
            sum1 += mat[i][i]
            sum1 += mat[r-i-1][i]
        if r % 2 == 1:
            c = (r-1)/2
            sum1-=mat[c][c]
        return sum1