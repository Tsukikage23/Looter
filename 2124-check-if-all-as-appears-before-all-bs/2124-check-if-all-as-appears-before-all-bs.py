class Solution(object):
    def checkString(self, s):
        count = 0
        for i in s:
            if i == "b":
                count = 1
            if i == "a" and count == 1:
                return False
        return True