class Solution(object):
    def reversePrefix(self, word, ch):
        if ch not in word:
            return word
        a = word.index(ch)
        b = word[:a+1][::-1]
        return b + word[a+1:]