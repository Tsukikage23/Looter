class Solution(object):
    def prefixCount(self, words, pref):
        a = 0
        b = len(pref)
        for i in range(len(words)):
            if len(words[i]) >= b:
                if words[i][:b] == pref:
                    a+=1
        return a