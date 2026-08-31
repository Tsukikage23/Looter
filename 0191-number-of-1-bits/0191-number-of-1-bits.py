class Solution(object):
    def hammingWeight(self, n):
        count = 0
        while n > 0:
            a = len(bin(n))-3
            n -= 2**a
            count+=1
        return count