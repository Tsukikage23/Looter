class Solution(object):
    def one(self,num):
        count = 0
        while num > 0:
            if num & 1 == 1:
                count += 1
            num >>= 1
        return count
    def hammingDistance(self, x, y):
        return self.one(x^y)