class Solution(object):
    def capitalizeTitle(self, title):
        a = title.split(" ")
        for i in range(len(a)):
            if len(a[i]) <= 2:
                a[i] = a[i].lower()
            else:
                a[i] = a[i].capitalize()
        return " ".join(a)