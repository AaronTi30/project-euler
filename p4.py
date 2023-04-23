## Project Euler 4: Largest palindrome product ##
# Find the largest palindrome made from the product of two 3-digit numbers. #

## Solution ##

# Define a function to check if a number is a palindrome
def is_palindrome(n):
    return str(n) == str(n)[::-1]


# Initialize variables to keep track of the largest palindrome and its factors
largest_palindrome = 0
largest_factors = (0, 0)

# Loop through all possible products of two 3-digit numbers
for i in range(100, 1000):
    for j in range(100, 1000):
        product = i * j
        # Check if the product is a palindrome and larger than the current largest palindrome
        if is_palindrome(product) and product > largest_palindrome:
            largest_palindrome = product
            largest_factors = (i, j)

# Print the largest palindrome and its factors
print("The largest palindrome made from the product of two 3-digit numbers is",
      largest_palindrome)
print("It is the product of", largest_factors[0], "and", largest_factors[1])
