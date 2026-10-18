class Solution(object):
    def splitNum(self, num):
        a = sorted(list(str(num)))
        b = ""
        c = ""
        for i in range(len(a)):
            if i%2==0:
                b+=a[i]
            else:
                c+=a[i]
        return int(b)+int(c)