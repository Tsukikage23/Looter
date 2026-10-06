class Solution(object):
    def balancedStringSplit(self, s):
        b = 0
        c = 0
        for i in s:
            if i == "R":
                c+=1
            else:
                c-=1
            if c == 0:
                b+=1
        return b