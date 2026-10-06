class Solution(object):
    def sumZero(self, n):
        a = list()
        b = n/2
        if n % 2 == 1:
            for i in range(-b,b+1):
                a.append(i)
        else:
            for i in range(-b,b+1):
                if i != 0:
                    a.append(i)
        return a