# project-euler problem 6 #
# Sum square difference #
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum. #

## Solution ##

# Initialize variables to store the sum of squares and the sum of the first 100 natural numbers
sum_of_squares = 0
sum = 0

# Iterate through the first 100 natural numbers and calculate the sum of squares and the sum of the numbers
for i in range(1, 101):
    sum_of_squares += i**2
    sum += i

# Calculate the square of the sum
square_of_sum = sum**2

# Calculate the difference between the sum of squares and the square of the sum
difference = square_of_sum - sum_of_squares

# Output the difference
print(difference)

## Output ##
# 25164150 #
