class Solution(object):
    def areNumbersAscending(self, s):
        words = s.split(" ")
        b = -1
        for i in words:
            if i.isdigit():
                a = int(i)
                if a <= b:
                    return False
                b = a
        return True