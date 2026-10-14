class Solution(object):
    def topKFrequent(self, nums, k):
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        a = list()
        for i in nums:
            count[i] = 1 + count.get(i,0)
        for i,j in count.items():
            freq[j].append(i)
        for i in range(len(freq)-1,0,-1):
            for j in freq[i]:
                a.append(j)
                if len(a) == k:
                    return a
        