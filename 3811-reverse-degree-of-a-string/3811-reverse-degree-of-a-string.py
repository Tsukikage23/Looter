class Solution(object):
    def reverseDegree(self, s):
        sum1 = 0
        for i in range(len(s)):
            sum1+=(i+1)*(ord("z")-ord(s[i])+1)
        return sum1