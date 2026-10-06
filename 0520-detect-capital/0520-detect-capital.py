class Solution(object):
    def detectCapitalUse(self, word):
        b = 0
        for i in range(len(word)):
            if word[i].isupper():
                b+=1
        if b == len(word) or b == 0:
            return True
        if word[0].isupper() and word[1:].islower():
            return True
        return False