class Solution(object):
    def findWordsContaining(self, words, x):
        a = list()
        for i in range(len(words)):
            if x in words[i]:
                a.append(i)
        return a