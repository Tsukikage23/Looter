class Solution(object):
    def countConsistentStrings(self, allowed, words):
        a = 0
        for i in words:
            if set(i) <= set(allowed):
                a+=1
        return a