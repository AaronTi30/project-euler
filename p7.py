## Project: Euler Problem 7: 10001st prime ##
# Question: What is the 10,001st prime number? #

## Explanation ##
# To find the 10,001st prime number, we need to generate prime numbers until we reach the desired number. #
# We can use a function to check if a given number is prime or not, and then iterate through numbers until we find the 10,001st prime number. #

## Solution ##

# Define a function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# Set a counter for the number of primes found
count = 0

# Set a variable for the current number being checked
current_num = 2

# Iterate through numbers until we find the 10,001st prime
while count < 10001:
    if is_prime(current_num):
        count += 1
        if count == 10001:
            print(current_num)
    current_num += 1

## Answer: 104743 ##
