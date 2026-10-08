class Solution(object):
    def sortVowels(self, s):
        a = list()
        b = ""
        for i in s:
            if i in "AEIOUaeiou":
                a.append(i)
        a.sort()
        j = 0
        for i in s:
            if i not in "AEIOUaeiou":
                b+=i
            else:
                b+=a[j]
                j+=1
        return b