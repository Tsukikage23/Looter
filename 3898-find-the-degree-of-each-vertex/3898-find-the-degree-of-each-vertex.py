class Solution(object):
    def findDegrees(self, matrix):
        a = list()
        for i in range(len(matrix)):
            a.append(sum(matrix[i]))
        return a