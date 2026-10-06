class Solution(object):
    def subtractProductAndSum(self, n):
        sum1 = 0
        prod = 1
        while n > 0:
            b = n%10
            sum1 += b
            prod *= b
            n //= 10
        return prod - sum1