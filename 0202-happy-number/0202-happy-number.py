class Solution(object):
    def square(self,n):
        a = len(str(n))
        sum1 = 0
        while n > 0:
            b = n%10
            sum1 += b**2
            n/=10
        return sum1
    def isHappy(self, n):
        c = set()
        while n != 1 and n not in c:
            c.add(n)
            n = self.square(n)

        if n == 1:
            return True
        return False