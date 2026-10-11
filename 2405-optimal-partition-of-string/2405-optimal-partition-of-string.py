class Solution(object):
    def partitionString(self, s):
        a = ""
        b = 0
        for i in s:
            if i not in a:
                a+=i
            elif i in a:
                b+=1
                a = ""
                a+=i
        if a:
            b+=1
        return b