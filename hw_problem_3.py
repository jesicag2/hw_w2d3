# HW1_P3: Advanced Slicing Techniques

# Task 1: Given the list of temperatures
# Extract the temperatures for the second week (7 days) of the month. Expected Outcome: 83, 85, 86, 87, 88, 89, 90,

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

second_week = temperatures[7:14]
print(second_week)


# Task 2: Extract all the temperatures above 100.

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

temperatures_above_100 = [temp for temp in temperatures if temp > 100]
print(temperatures_above_100)


# Task 3: Reverse the list and extract temperatures from the 5th to the 10th day of the reversed list.

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

temperatures.reverse()
print(temperatures)

temp_removed = temperatures[4:10]

for temp in temp_removed:
    temperatures.remove(temp)

print(temperatures)
