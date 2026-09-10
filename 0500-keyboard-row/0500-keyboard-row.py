class Solution(object):
    def findWords(self, words):
        a = set("qwertyuiop")
        b = set("asdfghjkl")
        c = set("zxcvbnm")
        d = list()
        for j in words:
            i = set(j.lower())
            if i <= a or i <= b or i <= c:
                d.append(j)
        return d