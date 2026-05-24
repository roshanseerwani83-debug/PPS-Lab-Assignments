# Read input
n = int(input())

# Initialize factorial
factorial = 1

# Calculate factorial using a loop
for i in range(1, n + 1):
    factorial *= i

# Print the factorial
print(factorial)
