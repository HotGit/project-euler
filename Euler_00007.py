# Project Euler 007
# Answer = 104,743

import time
import sys
import math

if len(sys.argv) < 2:
  parameter = 10001
else :  
  parameter = int(sys.argv[1])

print ('\nProject Euler Problem #7')
print ('Find the nth prime')
print ('Parameter:', parameter, '\n')

print('Brute force')
start_time = time.time()
counter = 3
primes = [2]
while len(primes) < parameter  :
  new_prime = True
  for prime in primes :
    if prime > math.sqrt(counter) :
      break
    if counter % prime == 0 :
      new_prime = False
      break
  if new_prime :
    primes.append(counter)
  counter += 2  
print('The', parameter,'th prime number is', primes[-1])
print("This took %s seconds\n" % (time.time() - start_time))

print('Sieve')
start_time = time.time()
upper_bound = int(parameter * (math.log(parameter) + math.log(math.log(parameter))))
sieve = [True] * upper_bound
for i in range(2, int(upper_bound ** (1/2))+1) :
  for j in range(2*i, upper_bound, i) :
     sieve[j] = False
primes = [i for i in range(2, upper_bound) if sieve[i]]
print('The',parameter,'th prime number is', primes[parameter - 1])
print("This took %s seconds\n" % (time.time() - start_time))

