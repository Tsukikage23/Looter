class Solution(object):
    def mostWordsFound(self, sentences):
        maxa = -1
        for i in range(len(sentences)):
            a = 1
            for j in range(len(sentences[i])):
                if sentences[i][j] == " ":
                    a+=1
            maxa = max(a,maxa)
        return maxa