class Solution(object):
    def reverseBits(self, n):
        a = ""
        b = bin(n)[2:]
        for i in b[::-1]:
            a+=i
        k = 32 - len(a)
        while k > 0:
            a+="0"
            k-=1
        return int(a,2)