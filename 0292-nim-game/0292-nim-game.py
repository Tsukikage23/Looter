class Solution(object):
    def canWinNim(self, n):
        if n <= 3:
            return True
        elif n%4==0:
            return False
        return True