class Solution(object):
    def isPalindrome(self, s):
        i = ""
        for k in range(len(s)):
            if s[k].isalnum():
                i+=s[k]
        return i.lower() == i[::-1].lower()