# Read marks for four subjects
marks = list(map(int, input().split()))

# Calculate total marks
total = sum(marks)

# Calculate aggregate percentage
aggregate = (total / 400) * 100  # Assuming each subject is out of 100

# Determine grade
if aggregate > 75:
    grade = "Distinction"
elif 60 <= aggregate <= 75:
    grade = "First Division"
elif 50 <= aggregate < 60:
    grade = "Second Division"
elif 40 <= aggregate < 50:
    grade = "Third Division"
else:
    grade = "Fail"

# Print results
print(total)
print(f"{aggregate:.2f}")
print(grade)
