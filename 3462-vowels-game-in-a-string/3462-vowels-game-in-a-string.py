class Solution(object):
    def doesAliceWin(self, s):
        c = 0
        for i in s:
            if i not in "aeiou":
                c+=1
        if c == len(s):
            return False
        return True