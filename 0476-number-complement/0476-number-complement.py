class Solution(object):
    def findComplement(self, num):
        a = len(bin(num)[2:])
        b = int(str(1)*a,2)
        return num^b