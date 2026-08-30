class Solution(object):
    def numSub(self, s):
        j = 0
        a = 0
        i = 0
        while j < len(s):
            if s[i] == "1" and s[j] == "1":
                a+=j-i+1
                j+=1
                continue
            elif s[j] != "1":
                j+=1
                i = j
        if a > 1000000007:
            return a % 1000000007
        return a