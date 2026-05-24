# Read sets from input
setA = set(map(int, input("Set A: ").split()))
setB = set(map(int, input("Set B: ").split()))

# Perform operations
union_set = setA | setB
intersection_set = setA & setB
difference_set = setA - setB

# Print results
print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference:", difference_set)
