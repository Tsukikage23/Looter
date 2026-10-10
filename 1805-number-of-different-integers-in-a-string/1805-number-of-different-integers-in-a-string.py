class Solution(object):
    def numDifferentIntegers(self, word):
        a = ""
        b = set()
        for i in word:
            if i.isdigit():
                a+=i
            else:
                if a:
                    c = int(a)
                    b.add(c)
                    a = ""
        if a:
            b.add(int(a))
        return len(b)