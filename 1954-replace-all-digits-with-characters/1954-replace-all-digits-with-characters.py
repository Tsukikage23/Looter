class Solution(object):
    def replaceDigits(self, s):
        ans = ""
        for i in range(len(s)):
            if s[i].isdigit():
                a = chr(ord(s[i-1])+int(s[i]))
                ans += a
            else:
                ans+=s[i]  
        return ans