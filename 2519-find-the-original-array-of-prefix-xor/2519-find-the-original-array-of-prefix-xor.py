class Solution(object):
    def findArray(self, pref):
        a = list()
        a.append(pref[0])
        for i in range(1,len(pref)):
            c = pref[i] ^ pref[i-1]
            a.append(c)
        return a