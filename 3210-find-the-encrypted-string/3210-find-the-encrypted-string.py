class Solution(object):
    def getEncryptedString(self, s, k):
        a = ""
        n = len(s)
        for i in range(n):
            a += s[(k+i)%n]
        return a