# num = int(input("Enter a number: "))
# cal = num%2
# print(f"Number is Odd: {bool(cal)}")


# age = int(input("Enter your age: "))
# print(f"{age}years = {age*365} days")


# minutes = int(input("Enter Minutes: "))
# print(f"{minutes} minutes is {minutes // 60}hours {minutes%60}minutes ")

# num = int(input("Enter Number: "))
# print(f"{num} : last digit is {num%10}")

#  comment added again
# role = input("Enter Role: ")
# age = int(input("Enter Age: "))

# role == "Student" and age < 21
# print(f"Eligible : {role.lower() == "student" and age < 21}")


# a = int(input("Enter number one: "))
# b = int(input("Enter number two: "))


# a = a + b
# b = a - b
# a = a - b


# print("a=", a)
# print("b=", b)


# is_Raining = False

# if is_Raining:
#     print("Raining Outside")
# else:
#     print("Not Raining")


# age = int(input("Enter your age: "))

# if age >= 18:
#     print("Eligible to vote")
# else:
#     print("Not Eligible to vote")


# n = int(input("Enter the number: "))

# if n == 1:
#     print("Sunday")
# elif n == 2:
#     print("Monday")
# elif n == 3:
#     print("Tuesday")
# elif n == 4:
#     print("Wednesday")
# elif n == 5:
#     print("Thursday")
# elif n == 6:
#     print("Friday")
# elif n == 7:
#     print("Saturday")
# else:
#   print("Please Enter between 1-7")


# age = 20
# id= True

# if age>18:
#   if id:
#     print("Entry")
#   else:
#     print("No Entry")
# else:
#   print("Underage")


# day = int(input("Enter number: "))

# match day:
#     case 1:
#         print("Sunday")
#     case 2:
#         print("Monday")
#     case 3:
#         print("Tuesday")
#     case 4:
#         print("Wednesday")
#     case 5:
#         print("Thursday")
#     case 6:
#         print("Friday")
#     case 7:
#         print("Saturday")
#     case _:
#         print("Enter Valid Number")


# num = int(input("Enter a number: "))
# if num%2 ==0:
#   print(f"Number {num} is Even.")
# else:
#   print(f"Number {num} is Odd.")


# ticket = 1000
# age = int(input("Enter Age: "))

# if age < 12:
#     print(f"Your ticket price is {ticket - ((ticket*10)/100)}")
# else:
#     print(f"Your ticket price is {ticket} ")


# marks = int(input("Enter Marks: "))

# if marks >= 90 and marks < 100:
#     print("Grade - 'O'")
# elif marks >= 80 and marks < 90:
#     print("Grade - 'A'")
# elif marks >= 65 and marks < 80:
#     print("Grade - 'B'")
# elif marks >= 35 and marks < 65:
#     print("Grade - 'C'")
# elif marks < 35 and marks >= 0:
#     print("Grade - 'F'")
# else:
#     print("Enter Valid Marks")


# num = int(input("Enter number: "))

# if num > 0:
#   print("Postive")
# elif num == 0:
#   print("Neutral")
# else:
#   print("Negative")


# a = int(input("Enter number A: "))
# b = int(input("Enter number B: "))
# c = int(input("Enter number C: "))


# if a >= b and a >= c:
#     print(f"{a} - A is greater")
# elif b >= a and b >= c:
#     print(f"{b} - B is greater")
# elif c >= a and c >= b:
#     print(f"{c} - C is greater")
# # elif a == b == c:
# #     print(f"All numbers are same")
# else:
#     print("Invalid")


# year = int(input("Enter year: "))

# if year % 4:
#     print(f"{year} is leap year.")
# else:
#     print(f"{year} is not a leap year.")


# a = int(input("Enter number A: "))
# b = int(input("Enter number B: "))
# choice = input("Enter Choice: ")

# match choice:
#     case "+":
#         print(f"Addition is {a + b}")
#     case "-":
#         print(f"Subtraction is {a - b}")
#     case "*":
#         print(f"Multiplication is {a * b}")
#     case "/":
#         if b == 0:
#             print("Cant divide by zero")
#         else:
#             print(f"Division is {a / b}")
#     case "%":
#         print(f"Remainder is {a % b}")
#     case _:
#         print("Invalid Choice")


# color = input("Enter signal color: ")

# if color == "red":
#     print("Stop")
# elif color == "yellow":
#     print("Get Ready")
# elif color == "green":
#     print("Go")
# else:
#     print("Invalid color")


# balance = 5000

# print("1. Check Balance")
# print("2. Deposit")
# print("3. Withdraw")
# print("4. Exit")

# choice = int(input("Enter your choice: "))

# if choice == 1:
#     print("Balance:", balance)

# elif choice == 2:
#     amount = int(input("Enter deposit amount: "))
#     balance = balance + amount
#     print("New balance:", balance)

# elif choice == 3:
#     amount = int(input("Enter withdrawal amount: "))

#     if balance >= amount:
#         balance = balance - amount
#         print("New balance:", balance)
#     else:
#         print("Insufficient balance")

# elif choice == 4:
#     print("Exit")

# else:
#     print("Invalid choice")


# user1 = input("Player 1 Enter Choice: ")
# user2 = input("Player 2 Enter Choice: ")


# if user1 == user2:
#     print("Draw")
# elif user1 == "rock" and user2 == "paper":
#     print("Print Player 2 Wins")
# elif user1 == "paper" and user2 == "rock":
#     print("Print Player 1 Wins")
# elif user1 == "scissor" and user2 == "paper":
#     print("Print Player 1 Wins")
# elif user1 == "paper" and user2 == "scissor":
#     print("Print Player 1 Wins")
# elif user1 == "rock" and user2 == "scissor":
#     print("Print Player 1 Wins")
# elif user1 == "scissor" and user2 == "rock":
#     print("Print Player 2 Wins")
# else:
#   print("Invalid Choice")
