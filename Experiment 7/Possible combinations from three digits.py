from itertools import permutations

# Read three digits
digits = input().split()  # Keep as strings to preserve leading zeros

# Generate all permutations of length 3
all_combinations = permutations(digits, 3)

# Print each combination as a 3-digit number
for combo in all_combinations:
    print(''.join(combo))
