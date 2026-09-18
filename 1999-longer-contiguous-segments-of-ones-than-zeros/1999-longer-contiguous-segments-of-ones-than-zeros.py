class Solution(object):
    def checkZeroOnes(self, s):
        streak1 = 0
        streak0 = 0
        a = 0
        b = 0
        for i in s:
            if i == "1":
                a+=1
                streak1 = max(streak1,a)
            elif i!="1":
                a = 0
        for i in s:
            if i == "0":
                b+=1
                streak0 = max(streak0,b)
            elif i!="0":
                b = 0
        return streak1>streak0