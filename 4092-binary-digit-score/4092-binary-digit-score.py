class Solution(object):
    def calculateScore(self, a, b):
        a1 = bin(a).count("1")
        b1 = bin(b).count("1")
        if a1 >= b1:
            return a1*b1
        return b1/a1