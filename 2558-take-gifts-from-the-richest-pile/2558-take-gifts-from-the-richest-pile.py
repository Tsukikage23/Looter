class Solution(object):
    def pickGifts(self, gifts, k):
        while k:
            a = max(gifts)
            b = int(math.floor(a**0.5))
            i = gifts.index(a)
            gifts[i] = b
            k-=1
        return sum(gifts)