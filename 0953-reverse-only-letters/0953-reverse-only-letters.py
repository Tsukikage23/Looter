class Solution(object):
    def reverseOnlyLetters(self, s):
        slist = list(s)
        i = 0
        j = len(slist) - 1
        while(i<=j):
            if slist[i].isalpha() and slist[j].isalpha():
                slist[i],slist[j] = slist[j],slist[i]
                i+=1
                j-=1
            elif not slist[i].isalpha() and slist[j].isalpha():
                i+=1
            elif slist[i].isalpha() and not slist[j].isalpha():
                j-=1
            else:
                i+=1
                j-=1
        return "".join(slist)