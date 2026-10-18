class Solution(object):
    def findClosest(self, x, y, z):
        a = abs(x-z)
        b = abs(y-z)
        if a==b:
            return 0
        elif a > b:
            return 2
        else:
            return 1