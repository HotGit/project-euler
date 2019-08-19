# Project Euler 001
# Answer = 233,168

import sys
import time

if len(sys.argv) < 2:
  threshold = 1000
else :  
  threshold = int(sys.argv[1])

print ('\nProject Euler Problem #1')
print ('Sum numbers less than a threshold divisible by 3 or 5')
print ('Threshold:', threshold, '\n')

def is_divisible(check_num, divisor) :
  return ((check_num % divisor) == 0)
    
def arithmetic_sum(check_num):
  return check_num*(check_num+1)/2

def sum_of_divisors(check_sum, divisor):
  times = int(check_sum / divisor)
  return int(divisor * arithmetic_sum(times))

print('Brute force')
start_time = time.time()
total = 0
counter = 1
while counter < threshold :
  if (is_divisible(counter, 3) or is_divisible(counter,5)) :
    total += counter
  counter += 1
print ('This collection sums to', total)
print('This took %s seconds\n' % (time.time() - start_time))

print('Lambda Filter')
start_time = time.time()
total = sum(list(filter(lambda x: not (x % 3) or not (x % 5), [x for x in range(1,threshold)])))
print ('This collection sums to', total)
print('This took %s seconds\n' % (time.time() - start_time))

print('One-liner')
start_time = time.time()
print ('This collection sums to', sum([x for x in range(1, threshold) if x % 3 == 0 or x % 5 ==0]))
print('This took %s seconds\n' % (time.time() - start_time))

print('Clever')
start_time = time.time()
total = sum_of_divisors(threshold - 1, 3) + sum_of_divisors(threshold - 1, 5) - sum_of_divisors(threshold - 1, 15)
print ('This collection sums to', total)
print('This took %s seconds\n' % (time.time() - start_time))
