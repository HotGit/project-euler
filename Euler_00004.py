# Project Euler 004
# Find largest palidromic number made as the product of two three digit numbers 
# Answer = 993 * 913 = 906,609

import sys
import time

print ('\nProject Euler Problem #4')
print ('Find largest palidromic number made as the product of two three digit numbers\n')

def is_palindrome(check_num) :
  check_string = str(check_num)
  return check_string == check_string[::-1]

def find_it() :
  answer = [0, 0 ,0]
  for i in range(999,99,-1) :
    for j in range(i,99,-1) :
      if i*j > answer[2] :
        if is_palindrome(i*j) :
          answer[0] = i
          answer[1] = j
          answer[2] = i*j
  return answer

# palindrome 'abccba' = a(10^5+10^0) + b(10^4+10^1) + c(10^3 + 10^2)
#                     = 100001 * a + 10010 * b + 1100 * c
#                     = 11 * (9901 * a + 910 * b + 100 * c)
#                     = product_1 * product_2
# At least one factor has to be a divisible by 11        
def better_find_it() :
  answer = [0, 0 ,0]
  for i in range(999,99,-1) :
    for j in range(i-i%11,99,-11 if i%11 else -1) :
      if i*j > answer[2] :
        if is_palindrome(i*j) :
          answer[0] = i
          answer[1] = j
          answer[2] = i*j
  return answer

 
print('Brute Force')  
start_time = time.time()
print('Largest product is', find_it())
print("This took %s seconds\n" % (time.time() - start_time))

print('Slightly better Brute Force exploiting palindrome\'s divisibility by 11')  
start_time = time.time()
print('Largest product is', better_find_it())
print("This took %s seconds\n" % (time.time() - start_time))

