class Solution(object):
    def isFascinating(self, n):
        a = str(2*n)
        b = str(3*n)
        d = str(n)+a+b
        c = set()
        if "0" in d:
            return False
        for i in d:
            if i not in c:
                c.add(i)
            else:
                return False
        return len(c) == 9