class Solution(object):
    def elevatorRequests(self, n, requests):
        a = 0
        for i in range(1,len(requests)):
            a += abs(requests[i] - requests[i-1])
        a += requests[0]
        return a