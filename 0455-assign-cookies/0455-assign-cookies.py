class Solution(object):
    def findContentChildren(self, g, s):
        l = 0
        r = 0
        gs = len(g)
        ss = len(s)
        g.sort()
        s.sort()
        while l < gs and r < ss:
            if g[l] <= s[r]:
                l+=1
            r+=1
        return l