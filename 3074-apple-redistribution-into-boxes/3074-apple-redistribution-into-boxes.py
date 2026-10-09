class Solution(object):
    def minimumBoxes(self, apple, capacity):
        a = sum(apple)
        capacity.sort()
        b = 0
        for i in capacity[::-1]:
            a-=i
            b+=1
            if a <= 0:
                return b
        return 1