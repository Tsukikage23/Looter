class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        n = len(strs)
        prefix = strs[0]
        for i in range(1,n):
            word = strs[i]
            leng = min(len(prefix),len(word))
            matchlen = 0
            for j in range(leng):
                if prefix[j] != word[j]:
                    break
                matchlen+=1
            prefix = prefix[:matchlen]
        if not prefix:
            return ""
        return prefix