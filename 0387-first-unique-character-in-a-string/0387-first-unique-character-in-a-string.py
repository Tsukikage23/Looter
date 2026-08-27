class Solution(object):
    def firstUniqChar(self, s):
        visited = list()
        if len(s) == 1:
            return 0
        for i in range(len(s)-1):
            if s[i] not in s[i+1:] and s[i] not in visited:
                return i
            visited.append(s[i])
        if s[-1] not in visited:
            return len(s)-1
        return -1