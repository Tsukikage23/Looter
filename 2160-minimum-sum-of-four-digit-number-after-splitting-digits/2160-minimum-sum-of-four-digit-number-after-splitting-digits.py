class Solution(object):
    def minimumSum(self, num):
        a = list()
        for i in str(num):
            a.append(int(i))
        a.sort()
        b = 0
        c = 0
        if a[1] == a[2]:
            b = a[0] * 10 + a[1]
            c = a[2] * 10 + a[3]
        else:
            b = a[0]*10 + a[2]
            c = a[1]*10 + a[3]
        # else:
            
        return b+c