class Solution(object):
    def sortSentence(self, s):
        a = s.split()
        b = [""]*len(a)
        for i in range(len(a)):
            word = a[i][:-1]
            b[int(a[i][-1])-1] = word
        return " ".join(b)