## Project Euler: Problem 5 ##
# Find the smallest positive number that is evenly divisible by all of the numbers from 1 to 20. #

# Define a function to check if a number is divisible by all numbers in a range
def is_divisible(num, start, end):
    for i in range(start, end+1):
        if num % i != 0:
            return False
    return True


# Start with the smallest number that can be divided by all numbers from 1 to 10
num = 2520

# Keep checking if the number is divisible by all numbers from 1 to 20
while not is_divisible(num, 1, 20):
    num += 2520  # increment by the smallest number that can be divided by 1 to 10

# Print the smallest number that is divisible by all numbers from 1 to 20
print(num)

## Output ##
# 232792560 #
