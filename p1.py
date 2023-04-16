## Project Euler Problem 1 - Multiples of 3 and 5 ##

## Problem Statement ##
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000. #

## Solution ##
# initialize sum to 0 and loop through all numbers from 1 to 999 ( 1 <= (3,5) <1000 ) #
# check number and if the number is divisible by 3 or 5, add it to the sum #
# print the sum #

sum = 0

for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        sum += i
print(sum)

# Output: 233168 #
