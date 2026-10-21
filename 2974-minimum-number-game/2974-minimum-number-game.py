class Solution(object):
    def numberGame(self, nums):
        a = list()
        c = list()
        n = len(nums)
        j = 0
        heapq.heapify(nums)
        for i in range(n):
            b = heapq.heappop(nums)
            a.append(b)
            j+=1
            if j == 2:
                c += a[::-1]
                j = 0
                a = []
        return c