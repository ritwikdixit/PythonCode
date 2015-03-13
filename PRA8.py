#For the number of test cases (T) on the first line:
#for the next T lines:
#Find out the probability that
#any proper divisor of N would be an even perfect square. 
#For each test case, print in a new line the output in p/q format where p
#and q are positive coprime integers. If p is 0, you should simply output 0.

#My Solution
#Ritwik Dixit 2015
#Homestead Programming Club
#Advanced Problem 8

from fractions import Fraction

def findDivisors(n):
    divisors = []
    for i in range(1, n - 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

def isEvenPerfectSquare(n):
    if (n ** 0.5).is_integer() and n % 2 == 0:
        return True
    return False

#num of inputs
n = int(raw_input())
results = []

for i in range(n):
    num = int(raw_input())
    divisors = findDivisors(num)

    #creating the fraction
    numerator = 0
    denominator = len(divisors)
    #if even perfect square add to numerator (probability)
    for divisor in divisors:
        if isEvenPerfectSquare(divisor):
            numerator += 1
    #create a fraction with the stuff
    f = Fraction(numerator, denominator)
    results.append(f)

#print results
for fraction in results:
    print fraction

        
        
