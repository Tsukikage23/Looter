class Solution(object):
    def minMovesToSeat(self, seats, students):
        seats.sort()
        students.sort()
        a = 0
        for i in range(len(seats)):
            a+= abs(seats[i]-students[i])
        return a