class Solution(object):
    def maximumOddBinaryNumber(self, s):
        c = 0
        d = 0
        for i in s:
            if i == "1":
                c+=1
            else:
                d+=1
        e = ""
        while c > 1:
            e += "1"
            c-=1
        while d > 0:
            e += "0"
            d-=1
        e+="1"
        return e