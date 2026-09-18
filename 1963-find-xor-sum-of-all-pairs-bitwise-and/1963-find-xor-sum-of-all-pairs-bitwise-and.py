class Solution(object):
    def getXORSum(self, arr1, arr2):
        a = 0
        b = 0
        for i in arr1:
            a^=i
        for j in arr2:
            b^=j
        return a&b