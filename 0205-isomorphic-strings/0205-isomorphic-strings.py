class Solution(object):
    def isIsomorphic(self, s, t):
        st = dict()
        ts = dict()
        for i in range(len(s)):
            cs = s[i]
            ct = t[i]
            if cs in st and st[cs] != ct:
                return False
            if ct in ts and ts[ct] != cs:
                return False
            st[cs] = ct
            ts[ct] = cs
        return True