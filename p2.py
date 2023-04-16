# Project Euler Problem 2 #
# q: By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms. #

# Initialize variables
a, b = 1, 2
sum_even = 0

# Loop until b exceeds 4 million
while b <= 4000000:
    # Check if b is even and add it to the sum
    if b % 2 == 0:
        sum_even += b
    # Calculate the next term in the sequence
    a, b = b, a + b

# Print the sum of even-valued terms
print(sum_even)
