class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        a = nums[::]
        heap = [(n,i) for i,n in enumerate(nums)]
        heapq.heapify(heap)
        for _ in range(k):
            n,i = heapq.heappop(heap)
            a[i] *= multiplier
            heapq.heappush(heap, (a[i],i))
        return a