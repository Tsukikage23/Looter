class Solution(object):
    def repeatedCharacter(self, s):
        a = set()
        for i in s:
            if i not in a:
                a.add(i)
            else:
                return i