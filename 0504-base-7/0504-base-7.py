class Solution(object):
    def convertToBase7(self, num):
        if num == 0:
            return "0"
        a = abs(num)
        c = []
        while a > 0:
            c.append(str(a%7))
            a//=7
        if num < 0:
            return "-"+"".join(c[::-1])
        return "".join(c[::-1])