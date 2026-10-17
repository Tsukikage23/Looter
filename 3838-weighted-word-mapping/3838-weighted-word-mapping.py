class Solution(object):
    def mapWordWeights(self, words, weights):
        a = ""
        for i in words:
            b = 0
            for j in i:
                b += weights[ord(j) - ord("a")]    
            b = b%26
            a += chr(ord("z") - b)
        return a