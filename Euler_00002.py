# Project Euler 002
# Answer = 4,613,732

import sys
import time

if len(sys.argv) < 2:
  threshold = 4000000
else :  
  threshold = int(sys.argv[1])

print ('\nProject Euler Problem #2')
print ('Sum even Fibonacci numbers up to and including a threshold')
print ('Threshold:', threshold, '\n')

def is_divisible(check_num, divisor) :
  return ((check_num % divisor) == 0)

print('Brute force')
start_time = time.time()
total, first, second = 0, 0, 1
latest = first + second
while latest <= threshold :
  if is_divisible(latest, 2) : 
    total += latest
  first, second = second, latest
  latest = first + second
print ('This collection sums to', total)
print('This took %s seconds\n' % (time.time() - start_time))

def even_fibs(check_num) :
  first, second = 0, 1
  while first <= check_num :
    if not first % 2 :
      yield first
    first, second = second, first + second

print('Generator')
start_time = time.time()
print ('This collection sums to', sum(even_fibs(threshold)))
print('This took %s seconds\n' % (time.time() - start_time))
