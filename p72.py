# Project Euler Probelem 72 #


def euler_phi(n):
    """
    Calculate Euler's Totient function (phi) for a given number n.
    """
    phi = n  # Initialize phi with n

    # Iterate over prime factors of n
    p = 2
    while p * p <= n:
        if n % p == 0:
            # p is a prime factor of n
            while n % p == 0:
                n //= p
            # Reduce phi using the formula (1 - 1/p)
            phi -= phi // p
        p += 1

    # If n has a prime factor greater than sqrt(n)
    if n > 1:
        phi -= phi // n

    return phi


def count_reduced_proper_fractions(limit):
    """
    Count the number of reduced proper fractions for d ≤ limit.
    """
    count = 0  # Initialize the count

    # Iterate over the denominators from 2 to the limit
    for d in range(2, limit + 1):
        count += euler_phi(d)  # Add Euler's Totient function value to the count

    return count


# Main program
limit = 1000000
result = count_reduced_proper_fractions(limit)
print("Number of reduced proper fractions for d ≤", limit, ":", result)
