class Solution(object):
    def isSumEqual(self, firstWord, secondWord, targetWord):
        a = ""
        for i in firstWord:
            a += str(ord(i)-ord("a"))
        b = ""
        for i in secondWord:
            b += str(ord(i)-ord("a"))
        c = ""
        for i in targetWord:
            c += str(ord(i)-ord("a"))
        return int(a) + int(b) == int(c)