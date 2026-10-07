class Solution(object):
    def convertTemperature(self, celsius):
        a = celsius + 273.15
        b = celsius * 1.80 + 32.00
        return [a,b]