class Solution(object):
    def countEven(self, num):
        c = 0
        for i in range(1,num+1):
            a = 0
            while i > 0:
                a+=i%10
                i//=10
            if a%2==0:
                c+=1
        return c