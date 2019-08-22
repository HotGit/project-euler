# Project Euler 028
# Answer = 669171001

import sys
import time

if len(sys.argv) < 2:
  square_size = 1001
else :  
  square_size = int(sys.argv[1])

if square_size % 2 == 0 :
  print ('\nRequires odd number\n')
  sys.exit()
  
print ('\nProject Euler Problem #28')
print ('Sum diagonals in a spiral square')
print ('Square size:', square_size, '\n')

print('Pattern Recognition')
print('For each concentric square of size n x n (n is an odd number),')
print('has smallest element of (n-2)^2 + 1 and largest element of n^2')
print('Contribution from concentric square is 4*(n-2)^2+(n-1)*10\n')

start_time = time.time()
total = 1
for i in range(3, square_size+1, 2) :
  total += 4*(i-2)**2 + (i-1) * 10

print ('The diagonal elements sum to', total)
print('This took %s seconds\n' % (time.time() - start_time))
