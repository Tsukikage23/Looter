class Solution(object):
    def maximumXor(self, s, t):
        a = t.count("0")
        b = t.count("1")
        c = ""
        for i in s:
            if i == "1":
                if a != 0:
                    c+="1"
                    a-=1
                else:
                    c+="0"
                    b-=1
            else:
                if b != 0:
                    c+="1"
                    b-=1
                else:
                    c+="0"
                    a-=1
        return c