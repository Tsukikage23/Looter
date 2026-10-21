class Solution(object):
    def lastStoneWeight(self, stones):
        a = [-s for s in stones]
        heapq.heapify(a)
        while len(a) > 1:
            b = -heapq.heappop(a)
            c = -heapq.heappop(a)
            if b != c:
                heapq.heappush(a, -abs(b - c))
        if not a:
            return 0
        return -a[0]