class Solution(object):
    def percentageLetter(self, s, letter):
        a = s.count(letter)
        n = len(s)
        return (a*100)/n