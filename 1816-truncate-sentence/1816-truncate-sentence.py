class Solution(object):
    def truncateSentence(self, s, k):
        words = s.split(" ")
        a = ""
        i = 0
        while k!=0:
            a += words[i]
            k-=1
            if k != 0:
                a+= " "
            i+=1
        return a