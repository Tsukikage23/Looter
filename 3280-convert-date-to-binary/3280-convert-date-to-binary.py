class Solution(object):
    def convertDateToBinary(self, date):
        a = ""
        b = date.split("-")
        a += bin(int(b[0]))[2:] + "-" + bin(int(b[1]))[2:] + "-" + bin(int(b[2]))[2:]
        return a