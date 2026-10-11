class Solution(object):
    def plusOne(self, digits):
        a = 0
        for i in digits:
            a = a*10+i
        b = list()
        a+=1
        while a > 0:
            b.append(a%10)
            a//=10
        return b[::-1]