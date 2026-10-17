class Solution(object):
    def findPeaks(self, mountain):
        a = list()
        for i in range(1,len(mountain)-1):
            if mountain[i-1] < mountain[i] and mountain[i] > mountain[i+1]:
                a.append(i)
        return a