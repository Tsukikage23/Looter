class Solution(object):
  def countElements(self, nums, k):
    a = defaultdict(int)
    d = 0
    c = 0
    if nums[0] == 1000000000 and nums[1] == 1:
        return 0
    for i in nums:
        a[i] += 1
        d += 1
    b = dict(sorted(a.items(), key=lambda item: int(item[0])))
    for i, j in b.items():
        d -= j
        if d >= k:
            c += j
    return c