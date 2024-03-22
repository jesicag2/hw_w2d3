# HW1_P4: Deep Dive into Python Lists

# Task 1: Given the lists
# Filter out students who have grades below 80. Print the name, grade and activiy. Expected Outcome "Jane", 78, "Art"

students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

for i in range(len(grades)):
    student = students[i]
    grade = grades[i]
    activity = activities[i]
    if grade < 80:
        print(f"{student}, {grade}, {activity}")


# Task 2: For the remaining students, add students name in a new list named students_approved. Expected Outcome: students_approved = ["John", "Doe", "Smith"]

students_approved = []

for i in range(len(grades)):
    student = students[i]
    grade = grades[i]
    activity = activities[i]
    if grade < 80:
        print(f"{student}, {grade}, {activity}")
    else:
        students_approved.append(student)


# Task 3: Print the list students_approved
        
print(students_approved)
