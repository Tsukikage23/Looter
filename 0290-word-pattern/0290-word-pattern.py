class Solution(object):
    def wordPattern(self, pattern, s):
        word = s.split(" ")
        a = dict()
        b = set()
        if len(word) != len(pattern):
            return False
        for i in range(len(word)):
            letter = pattern[i]
            w = word[i]
            if letter in a:
                if a[letter] != w:
                    return False
            else:
                if w in b:
                    return False
                a[letter] = w
                b.add(w)
        return True