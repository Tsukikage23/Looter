class Solution(object):
    def characterReplacement(self, s, k):
        ans = 0
        l = 0
        count = defaultdict(int)
        maxfreq = 0
        for r in range(len(s)):
            count[s[r]] += 1
            maxfreq = max(maxfreq,count[s[r]])
            if (r-l+1) - maxfreq > k:
                count[s[l]]-=1
                l+=1
            ans = max(ans,(r-l+1))
        return ans