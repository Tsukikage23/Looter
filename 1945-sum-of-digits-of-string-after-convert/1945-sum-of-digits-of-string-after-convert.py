class Solution(object):
    def getLucky(self, s, k):
        a = 0
        for i in s:
            b = ord(i) - ord("a") + 1
            while b > 0:
                a+=b%10
                b//=10
        k-=1
        while k > 0:
            c = 0
            while a > 0:
                c += a%10
                a//=10
            a = c
            k-=1
        return a