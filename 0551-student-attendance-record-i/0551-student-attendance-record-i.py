class Solution(object):
    def checkRecord(self, s):
        a = 0
        b = 0
        count = 0
        d = 0
        for i in s:
            if i == "A":
                count+=1
                a = 0
            elif i == "L":
                if a == 0:
                    b = 1
                    a = 1
                else:
                    b+=1
                d = max(b,d)
            else:
                a = 0
        if count >= 2 or d >= 3:
            return False
        return True