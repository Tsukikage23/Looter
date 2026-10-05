class Solution(object):
    def maximum69Number (self, num):
        a = 0
        b = 1
        for i in str(num):
            if i == "6" and b == 1:
                a = a*10 + 9
                b = 0
            else:
                a = int(i)+a*10
        return a