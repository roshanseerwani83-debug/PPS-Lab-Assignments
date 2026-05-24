import math

def is_prime(num):
    # Primes must be greater than 1
    if num < 2:
        return False
    # Check for factors from 2 up to the square root of num
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_in_range():
    try:
        start = int(input())
        end = int(input())
    except ValueError:
        return

    primes_found = []

    # Iterate through the range (inclusive)
    for val in range(start, end + 1):
        if is_prime(val):
            primes_found.append(val)

    # Output results
    if not primes_found:
        print("No primes")
    else:
        for prime in primes_found:
            print(prime)

if __name__ == "__main__":
    find_primes_in_range()
