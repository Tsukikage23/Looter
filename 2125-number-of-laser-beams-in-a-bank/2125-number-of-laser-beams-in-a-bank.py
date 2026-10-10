class Solution(object):
    def numberOfBeams(self, bank):
        prev = 0
        a = 0
        for i in bank:
            curr = i.count("1")
            if curr > 0:
                a+= prev*curr
                prev = curr
        return a