class Solution(object):
    def findTheDifference(self, s, t):
        dit = dict()
        for i in range(len(t)):
            if t[i] in dit:
                dit[t[i]] += 1
            else:
                dit[t[i]] = 1
        for i in range(len(s)):
            dit[s[i]] -= 1
        for key,value in dit.items():
            if value == 1:
                return key
        return "a"