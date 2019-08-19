# Project Euler 003
# Answer = 6,857

import sys
import time
import math

if len(sys.argv) < 2:
  number = 600851475143
else :  
  number = int(sys.argv[1])

print ('\nProject Euler Problem #3')
print ('Find largest prime factor of a given number')
print ('Number:', number, '\n')

print ('Build factor array and prime array')
start_time = time.time()
factors = []
# reduce by factors of two
while number % 2 == 0 :
  number = number / 2
  factors.append(2)
# reduce by factors of growing primes
odd_primes = []
counter = 3
while counter <= number :
  new_prime = True
  for prime in odd_primes :
    if prime > math.sqrt(counter) :
      break
    if counter % prime == 0 :
      new_prime = False
      break        
  if new_prime :
    odd_primes.append(counter)
    while number % counter == 0 :
      number = number / counter 
      factors.append(counter)
  counter += 2  
print ('The largest prime factor is', factors[-1])
print ('This took %s seconds\n' % (time.time() - start_time))

