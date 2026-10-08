class Solution(object):
    def firstPalindrome(self, words):
        for i in range(len(words)):
            a = words[i][::-1]
            if words[i] == a:
                return words[i]
        return ""