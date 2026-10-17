class Solution(object):
    def sumOfEncryptedInt(self, nums):
        c = list()
        for i in nums:
            b = 0
            d = 0
            while i > 0:
                a = i%10
                b = max(a,b)
                i//=10
                d += 1
            c.append(str(b)*d)
        e = 0
        for i in c:
            e += int(i)
        return e