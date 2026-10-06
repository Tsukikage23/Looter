class Solution(object):
    def getHint(self, secret, guess):
        bull = 0
        a = [0]*10
        b = [0]*10
        cow = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bull+=1
            else:
                a[int(secret[i])]+=1
                b[int(guess[i])]+=1
        for i in range(10):
            cow += min(a[i],b[i])
        return str(bull) + "A" + str(cow) + "B"