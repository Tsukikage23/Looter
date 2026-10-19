class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        a = max(candies)
        b = list()
        for i in candies:
            if i + extraCandies >= a:
                b.append(True)
            else:
                b.append(False)
        return b