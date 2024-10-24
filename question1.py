# Question 1(i)
# Write a Python program to find the distance between two coordinate points (x1, y1) and (x2, y2).

import math

x1 = int(input("Enter the x-value for the first cordinate: "))
y1 = int(input("Enter the y-value for the first cordinate: "))
x2 = int(input("Enter the x-value for the second cordinate: "))
y2 = int(input("Enter the y-value for the second cordinate: "))



distance = math.sqrt(((x2-x1)^2)+((y2-y1)^2))

print(distance)








# Question 1(ii)
# Write a Python program to find maximum between three numbers.

number_one = int(input("Enter the first number: "))
number_two = int(input("Enter the second number: "))
number_three = int(input("Enter the third number: "))

print(max(number_one, number_two, number_three))

