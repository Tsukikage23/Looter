class Solution(object):
    def reverseWords(self, s):
        a = list()
        word = s.split()
        for i in word:
            b = i[::-1]
            a.append(b)
        return " ".join(a)