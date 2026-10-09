class Solution(object):
    def maxFreqSum(self, s):
        a = [0]*26
        for i in s:
            a[ord(i)-ord("a")]+=1
        v = 0
        c = 0
        d = "aeiou"
        for i in range(len(a)):
            if chr(i + ord("a")) in d:
                v = max(v,a[i])
            else:
                c = max(c,a[i])
        return v+c