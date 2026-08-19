class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowel = set("aeiouAEIOU")
        slist = list(s)
        i = 0
        j = len(slist) - 1
        while(i<=j):
            if slist[i] in vowel and slist[j] in vowel:
                slist[i],slist[j] = slist[j],slist[i]
                i+=1
                j-=1
            elif slist[i] in vowel and slist[j] not in vowel:
                j-=1
            elif slist[i] not in vowel and slist[j] in vowel:
                i+=1
            else:
                i+=1
                j-=1
        return "".join(slist)