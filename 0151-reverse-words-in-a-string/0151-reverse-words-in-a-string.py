class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        word = s.split()
        i = 0
        j = len(word) - 1

        while i <= j:
            word[i],word[j] = word[j],word[i]
            i+=1
            j-=1
        
        return " ".join(word)