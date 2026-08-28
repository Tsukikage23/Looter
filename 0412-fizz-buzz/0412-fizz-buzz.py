class Solution(object):
    def fizzBuzz(self, n):
        a = [0]*n
        for i in range(n):
            if (i+1) % 3 == 0 and (i+1) % 5 == 0:
                a[i] = "FizzBuzz"        
            elif (i+1)% 3 == 0:
                a[i] = "Fizz" 
            elif (i+1) % 5 == 0:
                a[i] = "Buzz" 
            else:
                a[i] = str(i+1)
        return a