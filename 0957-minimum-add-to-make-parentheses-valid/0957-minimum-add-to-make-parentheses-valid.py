class Solution(object):
    def minAddToMakeValid(self, s):
        a = list()
        b = -1
        for i in s:
            if i == "(":
                a += "("
                b += 1
            elif i == ")":
                if b == -1:
                    a+=")"
                    b+=1
                    continue
                elif a[b] == "(":
                    a.pop()
                    b-=1
                    continue
                a += ")"
                b += 1
        return len(a)
                