'''
PROMPT:

Input:
The first line contains an integer n representing the number of points.
The next n lines each contains two integers x y representing the coordinates of the possible  points.


The best point is defined as the one that minimizes the sum of King distances between the chosen location
and the other n-1 points. The King distance between two points is defined as the number of steps it takes to go from one point to the other,
at each step travelling to one of the 8 surrounding lattice points (much like a King on a chessboard). For example, it takes one step to
go from (0, 0) to the points (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), and (-1,1).

Output:
Print the minimum total King distance of the best meeting point.

'''

#My Solution
#Ritwik Dixit 2015
#Homestead Programming Club
#Advanced Problem 12

def getKingsDistance(startx, starty, endx, endy):
    distance = 0
    while startx != endx or starty != endy:
        if startx < endx:
            startx += 1
        elif startx > endx:
            startx -= 1
        if starty < endy:
            starty += 1
        elif starty > endy:
            starty -= 1
        distance += 1
    return distance

points = []
numpoints = int(raw_input())
for i in range(numpoints):
    args = raw_input().split()
    points.append([int(args[0]), int(args[1])])

lowestkingsum = 1535000000000008080 #just a large number

for p in points:
    thiskingsum = 0
    for j in points:         #the coordinates
        if i != j:
            px = p[0]
            py = p[1]
            ex = j[0]
            ey = j[1]
            d = getKingsDistance(px, py, ex, ey)        
            thiskingsum += d
    if thiskingsum < lowestkingsum:
        lowestkingsum = thiskingsum

print lowestkingsum        
