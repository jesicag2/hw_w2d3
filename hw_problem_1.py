# HW1_P1: Python List Transformation

# Task 1: Given the list of grades
# Sort the grades in descending order and display the sorted list.

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

grades.sort()
grades.reverse()
print(grades)


#Task 2: Calculate the average grade and display it.

grade_total = 0
for grade in grades:
    grade_total += grade
print((grade_total) / len(grades))


#Task 3: Replace any grade below 80 with the value Failed.

for grade in grades:
    if grade >= 80:
        print(grade)
    else:
        print("Failed")
