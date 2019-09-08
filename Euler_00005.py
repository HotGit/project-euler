# Project Euler 005
# Answer = 232,792,560

import sys
import time
from functools import reduce

if len(sys.argv) < 2:
  parameter = 20
else :  
  parameter = int(sys.argv[1])

print ('\nProject Euler Problem #5')
print ('Smallest number that is divisible by all numbers 1 to parameter')
print ('Parameter:', parameter,'\n')

def gcd(a, b) :
  while b != 0 :
    a, b = b, a % b 
  return a

print('Lambda and Reduce')
start_time = time.time()
print('The answer is', int(reduce(lambda a,b: a * b / gcd(a,b), range(1,parameter+1))))
print("This took %s seconds\n" % (time.time() - start_time))

print('Same strategy but written loop (tends to outpace the reduce (Guido hates reduce))')
start_time = time.time()
answer = 1
for i in range(1, parameter + 1) :
  answer *= i / gcd(answer, i)
print('The answer is', int(answer))
print("This took %s seconds\n" % (time.time() - start_time))

