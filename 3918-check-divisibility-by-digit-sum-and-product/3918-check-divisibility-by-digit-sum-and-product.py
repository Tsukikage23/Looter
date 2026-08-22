class Solution(object):
    def checkDivisibility(self, n):
        a = n
        sum1 = 0
        pro = 1
        while a > 0:
            b = a%10
            sum1 += b
            pro *= b
            a/=10
        return n%(sum1+pro) == 0