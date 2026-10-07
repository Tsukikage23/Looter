class Solution(object):
    def maxDistinct(self, s):
        a = set()
        b = 0
        for i in s:
            if i not in a:
                a.add(i)
                b+=1
        return b