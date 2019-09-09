# Project Euler 006
# Answer =  25,164,150

import time
import sys

if len(sys.argv) < 2:
  parameter = 100
else :  
  parameter = int(sys.argv[1])

print ('\nProject Euler Problem #6')
print ('Difference between sum of squares and square of sums for 1 to parameter')
print ('Parameter:', parameter, '\n')

print('Brute force')
start_time = time.time()
counter = 1
sum_of_squares = 0
square_of_sums = 0
while counter <= parameter :
  sum_of_squares += counter**2
  square_of_sums += counter
  counter += 1
square_of_sums **= 2
print ('The square_of_sums is', square_of_sums)
print ('The sum_of_squares is', sum_of_squares)
print ('The difference is', square_of_sums - sum_of_squares)
print("This took %s seconds\n" % (time.time() - start_time))

