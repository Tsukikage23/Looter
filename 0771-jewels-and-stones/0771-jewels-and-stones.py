class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        a = 0
        for i in jewels:
            while i in stones:
                stones = stones.replace(i,"",1)
                a+=1
        return a