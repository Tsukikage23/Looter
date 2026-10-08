class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        a = x
        b = 0
        while a > 0:
            b += a % 10
            a//=10
        if x % b == 0:
            return b
        return -1