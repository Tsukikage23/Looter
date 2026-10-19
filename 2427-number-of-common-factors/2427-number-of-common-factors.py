class Solution(object):
    def commonFactors(self, a, b):
        e = 0
        c = min(a,b)
        d = max(a,b)
        for i in range(1,c+1):
            if c%i == 0 and d%i == 0:
                e+=1
        return e