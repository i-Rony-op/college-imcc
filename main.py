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


# while True:
#   string = input("Enter Pass: ")
#   if string=="raunak":
#     print("Matched")
#     break
#   else:
#     print("Not Matched")


# end = int(input("Enter the stop number: "))
# i = 0
# while i <= end:
#     print(i)
#     i = i + 1
#     if i == end:
#         break

# end = int(input("Enter the stop number: "))
# i = 0
# while i < end:
#     i = i + 1
#     if i % 2 ==0:
#       print(i)


# end = int(input("Enter the stop number: "))
# i = 0
# even = 0
# odd = 0
# while i < end:
#     if i % 2 == 0:
#         even = even + 1

#     else :
#         odd = odd + 1
#     i = i + 1

# print("Even", even)
# print("Odd", odd)


# i = 0
# while i < 10:
#     i = i + 1
#     if i == 5:
#         continue
#     print(i-1)


# n = int(input("Enter Number: "))
# i = 0
# while i <= 10:
#     print(f"{n} X {i} = {n*i}")
#     i = i + 1


# primes = []
# rangee = int(input("Enter Range: "))
# num = 2

# while num <= rangee:
#     i = 2
#     is_prime = True

#     while i < num:
#         if num % i == 0:
#             is_prime = False
#             break
#         i += 1

#     if is_prime:
#         primes.append(num)

#     num += 1

# print(primes)

# list = [1, 2, 3, 4, 2]
# sum = 0
# count = 0
# for i in list:
#     sum = sum + i
#     count = count + 1
# print("Sum: ", sum)
# print("Average: ", sum / count)

# while True:
#     print("1. Addition")
#     print("2. Subtraction")
#     print("3. Multiply")
#     print("4. Division")
#     print("5. Remainder")
#     print("6. Floor Division")
#     print("7. Power")
#     print("8. Factorial")
#     print("0. Exit")

#     choice = int(input("Enter your choice : "))

#     if choice == 1:
#         a = int(input("Enter 1st no. : "))
#         b = int(input("Enter 2nd no. : "))
#         print("Addition : ", a + b)

#     elif choice == 2:
#         a = int(input("Enter 1st no. : "))
#         b = int(input("Enter 2nd no. : "))
#         print("Subtraction : ", a - b)

#     elif choice == 3:
#         a = int(input("Enter 1st no. : "))
#         b = int(input("Enter 2nd no. : "))
#         print("Multiply : ", a * b)

#     elif choice == 4:
#         a = int(input("Enter 1st no. : "))
#         b = int(input("Enter 2nd no. : "))
#         if b == 0:
#             print("Cannot divide by zero")
#         else:
#             print("Division : ", a / b)

#     elif choice == 5:
#         a = int(input("Enter 1st no. : "))
#         b = int(input("Enter 2nd no. : "))
#         print("Remainder : ", a % b)

#     elif choice == 6:
#         a = int(input("Enter 1st no. : "))
#         b = int(input("Enter 2nd no. : "))
#         if b == 0:
#             print("Cannot divide by zero")
#         else:
#             print("Floor Division : ", a // b)

#     elif choice == 7:
#         a = int(input("Enter 1st no. : "))
#         b = int(input("Enter 2nd no. : "))
#         print("Power : ", a ** b)

#     elif choice==8:
#         a = int(input("Enter no. : "))
#         fac=1
#         for i in range(1,a+1):
#             fac=fac*i
#         print(fac)
#     elif choice==0:
#         break
#     else:
#         print("Invalid Choice")

# def printty(text):
#   print(text)


# printty("hello")


# def sum(a, b):
#   print ("SUM: ",a+b)

# sum(10 ,20)
# sum(20 ,20)
# sum(40 ,30)

# def pi():
#   return 3.14


# print(pi())


# def sum(a, b):
#   return a+b

# print(sum(10 ,20))


# def name(name= "r0ny"):
#   print("hello", name)

# name("raunak")
# name()

# a = int(input("Enter 1st no. : "))
# b = int(input("Enter 2nd no. : "))


# def calculator(a, b):
#     print("1. Addition")
#     print("2. Subtraction")
#     print("3. Multiply")
#     print("4. Division")
#     print("5. Remainder")

#     choice = int(input("Enter your choice : "))

#     if choice == 1:
#         print("Addition : ", a + b)
#     elif choice == 2:
#         print("Subtraction : ", a - b)
#     elif choice == 3:
#         print("Multiply : ", a * b)
#     elif choice == 4:
#         if b == 0:
#             print("Cannot divide by zero")
#         else:
#             print("Division : ", a / b)
#     elif choice == 5:
#         print("Remainder : ", a % b)
#     else:
#         print("Invalid Choice")


# calculator(a, b)


# def num(n):
#   print(n)
#   num(n-1)

# num(9)


# a = int(input("Enter no. : "))


# def factorial(a):
#     fac = 1
#     for i in range(1, a + 1):
#         fac = fac * i
#     print(fac)

# factorial(a)

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n - 1)


# num = int(input("Enter a number: "))

# print("Factorial:", factorial(num))


# square = lambda n: n * n
# print(square(8))

# add = lambda n, m: n + m
# print(add(8, 9))


# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print("*", end=" ")
#     print()

# for i in range(5, 0, -1):
#     for j in range(i):
#         print("*", end=" ")
#     print()


# for i in range(0, 6):
#     for j in range(0, i ):
#         print(j +1, end=" ")
#     print()

# for i in range(5, 0 , -1):
#     for j in range(0, i ):
#         print(j +1, end=" ")
#     print()

# x = 1
# for i in range(1, 7):
#     for j in range(0, i):
#         print(x, end=" ")
#         x += 1
#     print()

# print("----------------------------------------------------------")

# x = 21
# for i in range(6, 0, -1):
#     for j in range(0, i):
#         print(x, end=" ")
#         x -= 1
#     print()


# n = int(input("Enter Number: "))
# sum = 0
# for i in range(0, n + 1):
#     sum = sum + i

# print(sum)

# n = int(input("Enter NO: "))

# for i in range(1, n + 1):

#     for j in range(n - i):
#         print(" ", end="")

#     for k in range(2 * i - 1):
#         print("*", end="")

#     print()

# n = int(input("Enter NO: "))
# count = 0
# if n == 0:
#     print(1)
# else:
#     while n > 0:
#         n //= 10
#         count = count + 1
#     print(count)

# n = int(input("Enter Number: "))

# reverse = 0

# while n > 0:
#     digit = n % 10
#     reverse = reverse * 10 + digit
#     n //= 10
# print(reverse)

# x = -121
# n = x
# reverse = 0
# if x < 0:
#     print(bool(False))
# while x > 0:
#     digit = x % 10
#     reverse = reverse * 10 + digit
#     x //= 10
# if n == reverse:
#     print(bool(True))
# else:
#     print(bool(False))


# class Rectangle:
#     def __init__(self, x, y, width, height):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height


# rect = Rectangle(10, 20, 30, 40)
# print(rect.area())


# class Vector:
#     def __init__(
#         self,
#         x,
#         y,
#     ):
#         self.x = x
#         self.y = y

#     def getVector(self):
#         print(f"x = {self.x} y = {self.y} ")


# vec = Vector(10, 20)
# vec.getVector()


# class Shape:
#     def __init__(self, color):
#         self.color = color

#     def print_color(self):
#         print(self.color)


# class Rectangle(Shape):

#     def __init__(self, color, width, height):
#         super().__init__(color)
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height


# class Square(Rectangle):

#     def __init__(self, color, side):
#         super().__init__(color, side, side)


# s = Square("Blue", 5)
# r = Rectangle("Blue", 5, 9)

# print(r.area())
# s.print_color()
# print(s.area())
