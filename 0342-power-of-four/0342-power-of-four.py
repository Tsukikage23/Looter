class Solution(object):
    def isPowerOfFour(self, n):
        if n == 0:
            return False
        if n == 1: 
            return True
        if n % 4 != 0:
            return False
        result = self.isPowerOfFour(n//4)
        return result
        