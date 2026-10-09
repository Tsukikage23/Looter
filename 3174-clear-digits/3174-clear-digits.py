class Solution(object):
    def clearDigits(self, s):
        a = list()
        b = 0
        for i in s:
            if i.isalpha():
                a.append(i)
                b+=1
            else:
                if b > 0:
                    a.pop()
                    b-=1
                else:
                    a.append(i)
        return "".join(a)