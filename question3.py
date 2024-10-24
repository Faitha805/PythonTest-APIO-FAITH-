# Question 3(i)
#  Write a Python program that prompts a user to enter numbers. The process will repeat until
#  the user enters 0. Finally, the program prints sum of the numbers entered by the user.

#Number entry
user_number = 0
run = 1

while run == 1:
    user_number = int(input("Enter a number: "))
    sum += user_number

    if user_number != 0:
         print(f"The sum of the numbers entered is {sum}.")
         continue

    else:
        break

   







# Question 3(ii)
# Write a Python program to print all the numbers from 1 to 100 that are not divisible by 2

odd_numbers = range(1, 101, +2) 

