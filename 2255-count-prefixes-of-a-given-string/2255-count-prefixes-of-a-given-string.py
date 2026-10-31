class Solution(object):
    def countPrefixes(self, words, s):
        a = 0
        for i in range(len(words)):
            b = len(words[i])
            if s[:b] == words[i]:
                a+=1
        return a