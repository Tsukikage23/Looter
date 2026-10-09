class Solution(object):
    def decode(self, encoded, first):
        n = len(encoded)
        a = [0]*(n+1)
        a[0] = first
        b = a[0]
        for i in range(len(encoded)):
            b ^= encoded[i]
            a[i+1] = b
        return a