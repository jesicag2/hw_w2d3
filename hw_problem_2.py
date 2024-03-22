# HW1_P2: Advanced List Methods and Identity Operators

# Task 1: Given the two lists
# Find out which students both submitted their assignments and attended the class.

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

for student in submitted:
    if student in attended:
        print(student, "submitted assignement and attended class")


#Task 2: Check if the two lists are identical in terms of their content, regardless of order.

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

identical = True
for students in submitted:
    if student not in attended:
        identical = False
        break

if identical:
    print("The two lists are identical")
else:
    print("The two list are not identical")


#Task 3: Using list methods, remove any student from the attended list who did not submit their assignment.

for student in attended:
    if student not in submitted:
        attended.remove(student)

print(attended)
