class Solution(object):
    def countDigits(self, num):
        if num < 10:
            return 1
        a = 0
        b = num
        while b > 0:
            c = b%10
            if num%c == 0:
                a+=1
            b//=10
        return a