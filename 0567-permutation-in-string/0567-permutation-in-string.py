class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False
        counts1 = [0]*26
        counts2 = [0]*26
        for i in range(len(s1)):
            counts1[ord(s1[i]) - ord("a")]+=1
            counts2[ord(s2[i]) - ord("a")]+=1
        matches = 0
        for i in range(26):
            if counts1[i] == counts2[i]:
                matches+=1
        l = 0
        for i in range(len(s1),len(s2)):
            if matches == 26:
                return True
            b = ord(s2[i]) - ord("a")
            counts2[b]+=1
            if counts2[b] == counts1[b]:
                matches += 1
            elif counts2[b] == counts1[b] + 1:
                matches -= 1
            b = ord(s2[l]) - ord("a")
            counts2[b]-=1
            if counts2[b] == counts1[b]:
                matches += 1
            elif counts2[b] == counts1[b] -1:
                matches -= 1
            l+=1
        return matches == 26