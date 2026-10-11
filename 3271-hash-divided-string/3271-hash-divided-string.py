class Solution(object):
    def stringHash(self, s, k):
        a = ""
        b = 0
        c = k
        for i in s:
            b += ord(i) - ord("a")
            c-=1
            if c == 0:
                b = b % 26
                a += chr(ord("a") + b)
                c = k
                b = 0
        return a