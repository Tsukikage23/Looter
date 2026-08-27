class Solution(object):
    def lengthOfLastWord(self, s):
        i = str()
        a = []
        # for k in range(len(s)):
        #     if s[k] == " ":
        #         if i:
        #             a.append(i)
        #         i = str()
        #         continue
        #     i+=s[k]
        # if i:
        #     a.append(i)
        # return len(a[-1])
        for k in range(len(s)-1,-1,-1):
            if s[k] == " ":
                if i:
                    return len(i)
            else:
                i+=s[k]
        return len(i)