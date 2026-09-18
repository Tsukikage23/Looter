class Solution(object):
    def largestOddNumber(self, num):
        a = ""
        b = len(num)
        if b == 0:
            return a
        for i in range(len(num)-1,-1,-1):
            if int(num[i]) % 2 == 0:
                b = i
            else:
                break
        for i in range(b):
            a+=num[i]
        return a