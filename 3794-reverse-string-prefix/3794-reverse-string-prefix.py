class Solution(object):
    def reversePrefix(self, s, k):
        a = s[:k][::-1]
        return a + s[k:]