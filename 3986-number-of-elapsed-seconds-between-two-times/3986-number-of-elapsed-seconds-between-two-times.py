class Solution(object):
    def secondsBetweenTimes(self, startTime, endTime):
        a = startTime.split(":")
        b = endTime.split(":")
        c = int(b[0]) - int(a[0])
        d = int(b[1]) - int(a[1])
        e = int(b[2]) - int(a[2])
        c = c*3600
        d = d*60
        return c + d + e