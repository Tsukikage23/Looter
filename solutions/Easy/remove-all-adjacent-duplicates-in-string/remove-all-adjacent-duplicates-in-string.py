class Solution(object):
    def removeDuplicates(self, s):
        a = []
        for i in range(len(s)):
            if a and s[i] == a[-1]:
                a.pop()
            else:
                a.append(s[i])
        return "".join(a)
        