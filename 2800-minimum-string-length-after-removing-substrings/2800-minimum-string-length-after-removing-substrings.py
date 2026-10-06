class Solution(object):
    def minLength(self, s):
        a = 0
        while a == 0:
            if "AB" in s:
                s = s.replace("AB","")
            elif "CD" in s:
                s = s.replace("CD","")
            else: 
                a = 1
        return len(s)