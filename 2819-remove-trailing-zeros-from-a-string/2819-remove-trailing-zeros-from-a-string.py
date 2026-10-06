class Solution(object):
    def removeTrailingZeros(self, num):
        b = int(num)
        while b > 0:
            a = b%10
            if a == 0:
                b//=10
            else:
                return str(b)