# Project Euler problem 3 # Largest prime factor #
# The prime factors of 13195 are 5, 7, 13 and 29. # What is the largest prime factor of the number 600851475143 ? #

def isPrime(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n


print(isPrime(600851475143))


# Answer: 6857 #
# First, we initialize a variable i to 2, which is the smallest prime number. We then use a while loop to find the largest prime factor of n. #
# In each iteration of the loop, we check if i is a factor of n using the modulo operator (%). If n is not divisible by i, we increment i by 1 and continue the loop. If n is divisible by i, we divide n by i and update its value. #
# By doing this, we are effectively dividing n by all its prime factors until we are left with the largest prime factor, which is the value of n when the loop terminates. #
# The loop condition i * i <= n is used to limit the number of iterations. We only need to check the factors up to the square root of n, because any factor greater than the square root of n would have a corresponding factor that is less than the square root of n. For example, if n is 100 and we check the factors up to 10, we can find all the factors of n because any factor greater than 10 would have a corresponding factor less than 10. #
# Now, we can call the largest_prime_factor function with the number 600851475143 to find its largest prime factor: #
