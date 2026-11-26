class Solution(object):
    def canAliceWin(self, n):
        if n < 10:
            return False
        a = 0
        b = 10
        while True:
            if a == 0:
                if n >= b:
                    n -= b
                else:
                    return False
                a = 1
                b-=1
            elif a == 1:
                if n >= b:
                    n-=b
                else:
                    return True
                a = 0
                b-=1