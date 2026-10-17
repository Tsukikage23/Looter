class Solution(object):
    def minimumFlips(self, n):
        a = bin(n)[2:]
        b = len(a)
        c = 0
        for i in range(b//2):
            if a[i] != a[b-1-i]:
                c+=1
        return c*2