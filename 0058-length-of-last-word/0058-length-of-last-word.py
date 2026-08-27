class Solution(object):
    def lengthOfLastWord(self, s):
        i = str()
        a = []
        for k in range(len(s)):
            if s[k] == " ":
                if i:
                    a.append(i)
                i = str()
                continue
            i+=s[k]
        if i:
            a.append(i)
        return len(a[-1])