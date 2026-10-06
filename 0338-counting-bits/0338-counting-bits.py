class Solution(object):
    def countBits(self, n):
        a = list()
        a.append(0)
        for i in range(1,n+1):
            count = 0
            while i:
                i&=i-1
                count+=1
            a.append(count)
        return a