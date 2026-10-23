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


# n = int(input("Enter Number: "))

# prime = 0
# for i in range(1, n + 1):
#     if n % i == 0:
#         prime += 1

# if prime == 2:
#     print(f"{n} Prime No.")
# else:
#     print(f"{n} Not Prime No.")


# n = int(input("Enter Number: "))

# flag = 0
# for i in range(2, (n // 2) + 1):
#     if n % i == 0:
#         flag = 1
#         break

# if flag == 1:
#     print(f"{n} Not Prime No.")
# else:
#     print(f"{n} Prime No.")

# l = [2, 3, 5, 11, 9, 14, 18]
# mx = smax = float("-inf")
# mn = smin = float("inf")

# for i in l:
#     if i > mx:
#         smax, mx = mx, i
#     elif i > smax and i != mx:
#         smax = i

#     if i < mn:
#         smin, mn = mn, i
#     elif i < smin and i != mn:
#         smin = i

# print(f"MAX: {mx}")
# print(f"MIN: {mn}")
# print(f"SMAX: {smax}")
# print(f"SMIN: {smin}")


# num = int(input("Enter a Number: "))
# x = num
# reverse = 0
# sum = 0

# while num > 0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     sum += digit
#     num //= 10

# print(f"Sum of Digits is: {sum}")


# if reverse == x:
#     print("Number is Palindrme")
# else:
#     print("Number is not a Palindrme")

# num = int(input("Enter a Number: "))
# x = num
# sum = 0
# n = len(str(num))
# while num > 0:
#     digit = num % 10
#     sum += digit**n
#     num //= 10

# if sum == x:
#     print("Number is Armstrong")
# else:
#     print("Number is not a Armstrong")


# a = int(input("Enter a number : "))
# z = a
# b = 0
# c = 0
# while a>0:
#     c+=1
#     a//=10
# a = z

# while a>0:
#     b = b + (a%10)**c
#     a//=10

# if b == z:
#     print("The number is armstrong.")
# else:
#     print("The number is not armstrong.")


# num = int(input("Enter a Number: "))
# sum = 0
# for i in range(1, num + 1):
#     sum = (num * (num + 1) // 2) ** 2

# print(f"Sum of Digits is: {sum}")


# for i in range(5, 0, -1):
#     for j in range(i, 0, -1):
#         print(j, end=" ")
#     print()

# n = 5
# for i in range(1, n + 1):
#     for j in range(n, i - 1, -1):
#         print(j, end=" ")
#     print()


# Dictionary
# dict = {
#     "KEY1": "VALUE1",
#     "KEY2": "VALUE2",
#     "KEY3": "VALUE3",
#     "KEY4": "VALUE4",
# }
# print(dict["KEY1"])

# 1.Array Sum


# def read_array():
#     n = int(input("Enter N: "))
#     arr = []
#     for i in range(n):
#         value = int(input("Enter element " + str(i + 1) + ": "))
#         arr.append(value)
#     return arr


# arr = read_array()
# total = 0
# for x in arr:
#     total = total + x
# print("Sum =", total)


#  2.Largest, Second Largest, Smallest, Second Smallest

# arr = read_array()

# largest = arr[0]
# smallest = arr[0]
# for x in arr:
#     if x > largest:
#         largest = x
#     if x < smallest:
#         smallest = x

# second_largest = None
# for x in arr:
#     if x < largest:
#         if second_largest is None or x > second_largest:
#             second_largest = x

# second_smallest = None
# for x in arr:
#     if x > smallest:
#         if second_smallest is None or x < second_smallest:
#             second_smallest = x

# print("Largest         =", largest)
# print("Second largest  =", second_largest)
# print("Smallest        =", smallest)
# print("Second smallest =", second_smallest)


# 3.Count Even and Odd

# arr = read_array()
# even = 0
# odd = 0
# for x in arr:
#     if x % 2 == 0:
#         even = even + 1
#     else:
#         odd = odd + 1
# print("Even numbers =", even)
# print("Odd numbers  =", odd)


# 4.Search element

# arr = read_array()
# key = int(input("Enter number to search: "))

# found = False
# for i in range(len(arr)):
#     if arr[i] == key:
#         print(key, " at ", i + 1)
#         found = True

# if not found:
#     print(key, "not  in array")


# 5.Reverse array

# arr = read_array()

# print("Reverse order:", end=" ")

# for i in range(len(arr) - 1, -1, -1):
#     print(arr[i], end=" ")
# print()

# print("Original array:", arr)


# 6.Remove duplicates

# arr = read_array()
# unique = []
# for x in arr:
#     if x not in unique:
#         unique.append(x)
# print("Array without duplicates:", unique)


# 7.Move zeros
# arr = read_array()

# result = []
# zero_count = 0

# for x in arr:
#     if x == 0:
#         zero_count = zero_count + 1
#     else:
#         result.append(x)

# for i in range(zero_count):
#     result.append(0)

# print("After moving zeros:", result)


# 8.Patterns

# Pattern 1
# size = 7
# mid = size // 2
# for row in range(size):
#     for col in range(size):
#         if row == mid or col == mid:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


#  Pattern 2:
# n = 5
# for row in range(n):
#     for col in range(n):
#         if row == 0 or row == n - 1 or col == 0 or col == n - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


# Pattern 3
# n = 5
# size = 2 * n - 1
# mid = n - 1
# for row in range(size):
#     for col in range(size):
#         distance = abs(row - mid) + abs(col - mid)
#         if distance == mid:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


# Pattern 4
# n = 5
# for i in range(1, n + 1):
#     for s in range(n - i):
#         print(" ", end=" ")
#     for num in range(1, i + 1):
#         print(num, end=" ")
#     for num in range(i - 1, 0, -1):
#         print(num, end=" ")
#     print()


# Pattern 5
# n = 5
# for row in range(n):
#     for col in range(n):
#         if (row + col) % 2 == 0:
#             print(1, end=" ")
#         else:
#             print(0, end=" ")
#     print()


# 9. Count vowels, consonants, digits, special characters
# text = input("Enter a string: ")
# vowels = 0
# consonants = 0
# digits = 0
# special = 0

# for ch in text:
#     if ch.isalpha():
#         if ch.lower() in "aeiou":
#             vowels = vowels + 1
#         else:
#             consonants = consonants + 1
#     elif ch.isdigit():
#         digits = digits + 1
#     else:
#         special = special + 1

# print("Vowels             =", vowels)
# print("Consonants         =", consonants)
# print("Digits             =", digits)
# print("Special characters =", special)


# 10. Find all occurrences of a substring

# text = input("Enter the main string: ")
# sub = input("Enter the substring: ")

# count = 0
# for i in range(len(text) - len(sub) + 1):
#     if text[i:i + len(sub)] == sub:
#         count = count + 1
#         print("Found at index", i)

# print("Total occurrences =", count)


# 11. Reverse word
# sentence = input("Enter a sentence: ")
# words = sentence.split()

# result = ""
# for word in words:
#     reversed_word = ""
#     for ch in word:
#         reversed_word = ch + reversed_word
#     result = result + reversed_word + " "

# print(result.strip())


# 12. Longest , shortest word
# sentence = input("Enter a sentence: ")
# words = sentence.split()

# longest = words[0]
# shortest = words[0]

# for word in words:
#     if len(word) > len(longest):
#         longest = word
#     if len(word) < len(shortest):
#         shortest = word

# print("Longest word  =", longest)
# print("Shortest word =", shortest)

# print("-----------list-------------------------")
# l=[10,20,30,40]
# print(l)

# l.append(50)
# print(l)

# l.insert(3,500)
# print(l)

# l.remove(20)
# print(l)

# l.sort()
# print(l)

# l.reverse()
# print(l)

# print("-----------String-------------------------")
# str="Hello World"

# print(str.upper())
# print(str.lower())
# print(str.find("Hello"))
# print(str.split())
# print(str.replace("World","Mam"))

# 1. sum of 10 even nos
# sum = 0
# for i in range(1,11):
#   if i % 2 == 0:
#     sum += i
#     print(i)

# print(sum)

# 2. Squares
# s = int(input("Enter start  number: "))
# n = int(input("Enter end number: "))

# for i in range(s, s + n + 1):
#     print(i, " : ", i**2)

# 3. Reverse string
# s = input("Enter the string: ")
# print(s[::-1])

# 4. count vowels

# s = input("Enter the string: ")
# vow = "aeiou"

# count = 0
# for i in s.lower():
#   if i in vow:
#     count+=1

# print("Vowels: ", count)

# 5. duplicates from a list

# l = [1, 3, 4, 1, 3, 4, 6, 7, 6, 8]

# for i in range(len(l) - 1, -1, -1):
#     for j in range(i):
#         if l[i] == l[j]:
#             l.pop(i)
#             break

# print(l)

# 6. reverse a list

# l = [1,3,4,1,3,4,6,7,6,8]
# l.reverse()
# print(l)


# 7. pattern

# for i in range(1,6):
#   for j in range(1,i+1):
#     print("*", end=" ")
#   print()


# 8. pattern

# for i in range(1, 6):
#     if i % 2 == 1:
#         symbol = "*"
#     else:
#         symbol = "#"
#     space = 5 - i
#     stars = 2 * i - 1
#     print(" " * space, symbol * stars)

# 9. counts vowels count
# s= input("Enter String: ")
# vowels = "aeiouAEIOU"
# count=0
# hm={}
# for i in s:
#     if i in vowels:
#         hm[i] = hm.get(i, 0) + 1

# for i in hm:
#     print(i," : ",hm[i])


# for i in range(6):
#   for j in range(i):
#     print(chr(65+j), end=" ")
#   print()


# for i in range(5):
#   for j in range(i+1):
#     print(chr(65+i), end=" ")
#   print()

# num = 0
# for i in range(5):
#   for j in range(i+1):
#     print(chr(65+num), end=" ")
#     num += 1
#   print()
# num = 0
# for i in range(5):
#     print(" "*(5-i+1), end=" ")
#     for j in range(2*i+1):
#       print(chr(65+j), end=" ")
#     print()


# single linear linked list
# class Node:
#     def __init__(self, value):
#         self.data = value
#         self.next = None


# class SingleLinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, new_node):
#         if self.head == None:
#             self.head = new_node
#         else:
#             temp = self.head
#             while temp.next != None:
#                 temp = temp.next
#             temp.next = new_node

#     def print(self):
#         temp = self.head
#         while temp:
#             print(temp.data)
#             temp = temp.next

#     def insert_at_pos(self, pos, new_node):
#         if pos == 1:
#             new_node.next = self.head
#             self.head = new_node
#         else:
#             p = 1
#             temp = self.head
#             while p != pos - 1:
#                 temp = temp.next
#                 p += 1
#         new_node.next = temp.next
#         temp.next = new_node

#     def delete(self, value):
#         temp = self.head
#         prev = None
#         if temp.data == value:  # first node to delete
#             self.head = self.head.next
#         else:
#             while temp.data != value:
#                 prev = temp
#                 temp = temp.next
#                 if temp == None:
#                     print("Value is not Present in the list")
#                     return
#             prev.next = temp.next
#             temp = None


# list1 = SingleLinkedList()
# n1 = Node(10)
# n2 = Node(20)
# list1.append(n1)
# list1.append(n2)
# list1.append(Node(30))
# list1.append(Node(40))
# list1.insert_at_pos(3, Node(100))
# list1.delete(10)

# list1.print()
# print("---------------")
# list1.delete(2000)
# list1.print()


# str = "Raunak"
# count = 0
# for i in str.lower() :
#   if "a" in str:
#     count+= 1
# print(count)


# print the sum of last 4 elements of  the list
# find out the differenece between min and max element of the list
# insert a number in list , at 6th posi , this number must be 1/3 of number stored at 4th position


# last 4

# s = [1,2,34,5,5,6,7,7,8,8,8]


# print(f"Sum: {s[-1]+s[-2]+s[-3]+s[-4]}")


# # diffeerence in min max
# numbers = [10, 5, 25, 8, 15]

# min = min(numbers)
# max = max(numbers)

# difference = max - min

# print(difference)


# # insert at 6

# numbers = [10, 20, 30, 60, 50, 70, 80]

# number = numbers[3] / 3

# numbers.insert(5, number)

# print(numbers)


# import random


# students = {
#     101: {"Name": "Aditi", "Scores": [78, 85, 90]},
#     102: {"Name": "Rahul", "Scores": [45, 60, 50]},
#     103: {"Name": "Sneha", "Scores": [90, 88, 95]},
#     104: {"Name": "Karan", "Scores": [55, 72, 68]},
#     105: {"Name": "Priya", "Scores": [49, 51, 47]},
# }

# for sid, details in students.items():
#     avg = sum(details["Scores"]) / len(details["Scores"])
#     details["Average"] = avg
#     details["Passed"] = avg >= 50

# print("Students Who Passed: ")
# for sid, details in students.items():
#     if details["Passed"] == True:
#         print(details["Name"])

# # wap to guess a number and give reward
# user = int(input("Enter Number between 1 to 10 : "))
# num = random.randint(1,10)
# if user == num:
#   print("Yayyyyyyy")
# else:
#   print("asafdagghjkerfjgcdxsghjk")

# dict library

#  vowel with z
# s = input("Enter the Name: ")
# vowels = "aeiou"
# for i in s:
#     if i.lower() in vowels:
#         s = s.replace(i, "z")
# print(s)

#  list of numbers and string , accept from user , seperate the list from the max number , display the name in a desc order


# n = int(input("Enter the size of the List: "))
# list = []
# for i in range(0, n):
#     choice = input("Enter n for number and s for string: ")

#     if choice == "n":
#         value = int(input("Enter the number: "))
#         list.append(value)
#     else:
#         value = input("Enter the string: ")
#         list.append(value)

# print("Orignal List: ", list)

# numbers = []
# for i in list:
#     if type(i) == int:
#         numbers.append(i)

# maximum = max(numbers)
# indexofmax = list.index(maximum)

# l1 = list[:indexofmax]
# l2 = list[indexofmax:]

# print("List before maximum:", l1)
# print("List from maximum:", l2)


# numbers.sort(reverse=True)

# print("Numbers in descending order:", numbers)


# def solution():
#     class Node:
#         def __init__(self, data):
#             self.data = data
#             self.next = None

#     class LinkedList:
#         def __init__(self):
#             self.head = None

#         def create(self, values):
#             for value in values:
#                 self.insert(value, self.length())

#         def length(self):
#             count = 0
#             current = self.head
#             while current:
#                 count += 1
#                 current = current.next
#             return count

#         def insert(self, value, position):
#             new_node = Node(value)
#             if position <= 0 or self.head is None:
#                 new_node.next = self.head
#                 self.head = new_node
#                 return

#             current = self.head
#             index = 0
#             while current.next and index < position - 1:
#                 current = current.next
#                 index += 1

#             new_node.next = current.next
#             current.next = new_node

#         def traverse(self):
#             result = []
#             current = self.head
#             while current:
#                 result.append(str(current.data))
#                 current = current.next
#             return " ".join(result)

#         def middle(self):
#             slow = fast = self.head
#             if not slow:
#                 return None
#             while fast and fast.next:
#                 slow = slow.next
#                 fast = fast.next.next
#             return slow.data

#         def delete(self, value):
#             if not self.head:
#                 return

#             if self.head.data == value:
#                 self.head = self.head.next
#                 return

#             current = self.head
#             while current.next:
#                 if current.next.data == value:
#                     current.next = current.next.next
#                     return
#                 current = current.next

#         def reverse(self):
#             previous = None
#             current = self.head
#             while current:
#                 next_node = current.next
#                 current.next = previous
#                 previous = current
#                 current = next_node
#             self.head = previous

#         def consecutive_sums(self):
#             sums = []
#             current = self.head
#             while current and current.next:
#                 sums.append(str(current.data + current.next.data))
#                 current = current.next
#             return " ".join(sums)

#         def delete_first(self):
#             if self.head:
#                 self.head = self.head.next

#         def delete_last(self):
#             if not self.head:
#                 return
#             if not self.head.next:
#                 self.head = None
#                 return
#             current = self.head
#             while current.next.next:
#                 current = current.next
#             current.next = None

#     ll = LinkedList()
#     ll.create([1, 2, 3, 4, 5])

#     print("Linked List:", ll.traverse())

#     ll.insert(10, 2)
#     print("After Insertion:", ll.traverse())

#     print("Middle Node:", ll.middle())

#     ll.delete_first()
#     print("After Deleting First:", ll.traverse())

#     ll.delete_last()
#     print("After Deleting Last:", ll.traverse())

#     ll.delete(10)
#     print("After Deletion:", ll.traverse())

#     ll.reverse()
#     print("Reversed List:", ll.traverse())

#     print("Consecutive Sums:", ll.consecutive_sums())


# if __name__ == "__main__":
#     solution()


# # 1. Count vowels in a file
# with open("data.txt") as f:
#     text = f.read()
# count = sum(1 for ch in text.lower() if ch in "aeiou")
# print("Vowels:", count)


# # 2. Lines into a list; total, 2nd and 4th line
# with open("data.txt") as f:
#     lines = f.readlines()
# print("Total lines:", len(lines))
# if len(lines) >= 2:
#     print("2nd line:", lines[1].strip())
# if len(lines) >= 4:
#     print("4th line:", lines[3].strip())


# # 3. Sentence words list, longest word
# sentence = input("Enter a sentence: ")
# words = sentence.split()
# print(words)
# print("Longest word:", max(words, key=len))


# # 4. File words list
# with open("data.txt") as f:
#     words = f.read()
#     length = words.split()
# print("Total words:", len(length))
# print("Unique words:", set(length))

# def solution():
#     class Node:
#         def __init__(self, data):
#             self.data = data
#             self.next = None

#     class CircularLinkedList:
#         def __init__(self):
#             self.head = None
#             self.tail = None

#         def create(self, values):
#             for value in values:
#                 self.insert(value, self.length())

#         def length(self):
#             if not self.head:
#                 return 0
#             count = 1
#             current = self.head.next
#             while current is not self.head:
#                 count += 1
#                 current = current.next
#             return count

#         def insert(self, value, position):
#             new_node = Node(value)
#             if self.head is None:
#                 new_node.next = new_node
#                 self.head = self.tail = new_node
#                 return
#             if position <= 0:
#                 new_node.next = self.head
#                 self.tail.next = new_node
#                 self.head = new_node
#                 return
#             current = self.head
#             index = 0
#             while current is not self.tail and index < position - 1:
#                 current = current.next
#                 index += 1
#             new_node.next = current.next
#             current.next = new_node
#             if current is self.tail:
#                 self.tail = new_node

#         def traverse(self):
#             if not self.head:
#                 return ""
#             result = []
#             current = self.head
#             while True:
#                 result.append(str(current.data))
#                 current = current.next
#                 if current is self.head:
#                     break
#             return " ".join(result)

#         def middle(self):
#             if not self.head:
#                 return None
#             current = self.head
#             for _ in range(self.length() // 2):
#                 current = current.next
#             return current.data

#         def delete_first(self):
#             if not self.head:
#                 return
#             if self.head is self.tail:
#                 self.head = self.tail = None
#                 return
#             self.head = self.head.next
#             self.tail.next = self.head

#         def delete_last(self):
#             if not self.head:
#                 return
#             if self.head is self.tail:
#                 self.head = self.tail = None
#                 return
#             current = self.head
#             while current.next is not self.tail:
#                 current = current.next
#             current.next = self.head
#             self.tail = current

#         def delete(self, value):
#             if not self.head:
#                 return
#             if self.head.data == value:
#                 self.delete_first()
#                 return
#             current = self.head
#             while current.next is not self.head:
#                 if current.next.data == value:
#                     if current.next is self.tail:
#                         self.tail = current
#                     current.next = current.next.next
#                     return
#                 current = current.next

#         def reverse(self):
#             if not self.head:
#                 return
#             previous = self.tail
#             current = self.head
#             for _ in range(self.length()):
#                 next_node = current.next
#                 current.next = previous
#                 previous = current
#                 current = next_node
#             self.head, self.tail = self.tail, self.head

#         def consecutive_sums(self):
#             n = self.length()
#             if n < 2:
#                 return ""
#             sums = []
#             current = self.head
#             for _ in range(n):
#                 sums.append(str(current.data + current.next.data))
#                 current = current.next
#             return " ".join(sums)

#     cl = CircularLinkedList()
#     cl.create([1, 2, 3, 4, 5])
#     print("Circular List:", cl.traverse())

#     cl.insert(10, 2)
#     print("After Insertion:", cl.traverse())

#     print("Middle Node:", cl.middle())

#     cl.delete_first()
#     print("After Deleting First:", cl.traverse())

#     cl.delete_last()
#     print("After Deleting Last:", cl.traverse())

#     cl.delete(10)
#     print("After Deletion:", cl.traverse())

#     cl.reverse()
#     print("Reversed List:", cl.traverse())

#     print("Consecutive Sums:", cl.consecutive_sums())
#     print("Circular check:", cl.tail.next is cl.head)


# if __name__ == "__main__":
#     solution()


# # Double linear linked list
# class Node:
#     def __init__(self, value):
#         self.prev = None
#         self.data = value
#         self.next = None


# class DoubleLinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, new_node):
#         if self.head is None:
#             self.head = new_node
#             return
#         temp = self.head
#         while temp.next is not None:
#             temp = temp.next
#         temp.next = new_node
#         new_node.prev = temp

#     def display(self):
#         temp = self.head
#         while temp:
#             print(temp.data, end="->")
#             temp = temp.next
#         print()

#     def display_reverse(self):
#         if self.head is None:
#             print("Empty List!")
#             return
#         temp = self.head
#         while temp.next is not None:
#             temp = temp.next
#         while temp:
#             print(temp.data, end="->")
#             temp = temp.prev
#         print()

#     def insert_at_pos(self, pos, new_node):
#         if pos < 1:
#             print("Invalid position")
#             return
#         if pos == 1:
#             new_node.next = self.head
#             if self.head:
#                 self.head.prev = new_node
#             self.head = new_node
#             return
#         p = 1
#         temp = self.head
#         while temp and p != pos - 1:
#             temp = temp.next
#             p += 1
#         if temp is None:
#             print("Position out of range")
#             return
#         new_node.next = temp.next
#         new_node.prev = temp
#         if temp.next:
#             temp.next.prev = new_node
#         temp.next = new_node

#     def delete(self, value):
#         if self.head is None:
#             print("Empty List!")
#             return
#         temp = self.head
#         while temp and temp.data != value:
#             temp = temp.next
#         if temp is None:
#             print("Value is not Present in the list")
#             return
#         if temp.prev:
#             temp.prev.next = temp.next
#         else:
#             self.head = temp.next
#         if temp.next:
#             temp.next.prev = temp.prev

#     def reverse(self):
#         curr = self.head
#         prev = None
#         while curr:
#             nex_node = curr.next
#             curr.next = curr.prev
#             curr.prev = nex_node
#             prev = curr
#             curr = nex_node
#         self.head = prev

#     def first_last_node_del(self):
#         if self.head is None:
#             print("Empty List!")
#             return
#         if self.head.next is None:
#             self.head = None
#             return
#         self.head = self.head.next
#         self.head.prev = None
#         if self.head.next is None:
#             self.head = None
#             return
#         # remove last
#         temp = self.head
#         while temp.next is not None:
#             temp = temp.next
#         temp.prev.next = None


# list1 = DoubleLinkedList()
# list1.append(Node(10))
# list1.append(Node(20))
# list1.append(Node(30))
# list1.append(Node(40))
# list1.insert_at_pos(3, Node(100))
# list1.delete(10)

# list1.display()
# print("---------------")
# list1.delete(2000)
# list1.display()
# # list1.reverse()
# print("-------------------")
# list1.display()
# print("-----------------")
# list1.first_last_node_del()
# list1.display()
# list1.display_reverse()


# def greet(name):
#     print("Hello", name)


# n = int(input("Enter Number: "))
# m = int(input("Enter Number: "))


# def number(x, y):
#     return x % y

# print(number(n, m))


# n = int(input("Enter Number: "))


# def table(x):
#   for i in range(11):
#     print(f"{x} X {i} = {x*i}")


# table(n)


# def get_max(*num):
#   if len(num) == 0:
#     print(None)
#   max = num[0]
#   for i in num:
#     if i > num[0]:
#       max = i
#   print( max)

# get_max(12,3,3,4,15)


# def get_long(*str):
#     if len(str) == 0:
#         print(None)
#     max = str[0]
#     for i in str:
#         if i > str[0]:
#             max = i
#     print(max)


# get_long("hello", "hi", "r0ny", "raunak", "radheshyam", "radheshyan")


# class Node:
#     def __init__(self, value):
#         self.data = value
#         self.next = None


# class Stack:
#     def __init__(self):
#         self.top = None

#     def isEmpty(self):
#         return self.top is None

#     def push(self, node):
#         node.next = self.top
#         self.top = node

#     def pop(self):
#         if self.isEmpty():
#             print("Stack is Empty")
#         else:
#             temp = self.top
#             print("Popped Element", temp.data)
#             self.top = self.top.next
#             temp = None

#     def reverse(self):
#       temp = self.data
#       while temp:
#         st1.push(Node(temp.data))
#         temp = temp.next
        

#     def print(self):
#         temp = self.top
#         print("Stack Elements....")
#         while temp:
#             print(temp.data)
#             temp = temp.next


# st = Stack()
# st1 = Stack()

# st.push(Node(10))
# st.push(Node(20))
# st.push(Node(30))
# st.push(Node(40))
# st.push(Node(50))
# st.print()
# st.pop()
# st.pop()
# st.print()


# class Node:
#   def __init__(self, value):
#     self.data = value
#     self.next = None

# class LQ:
#   def __init__(self):
#     self.front = self.rear = None

#   def enqueue(self, node):
#     if self.rear:
#       self.rear.next = node
#       self.rear = node
#     else:
#       self.front = self.rear = node
#   def dequeue(self):
#     if self.front:
#       temp = self.front
#       self.front = self.front.next
#       if self.front == None:
#         self.rear = None
#         print("Now Queue is Empty")
#       temp = None
#     else:
#       print("Queue is Empty....!")
  
#   def print(self):
#     temp = self.front
#     while temp:
#       print(temp.data, end=" ")
#       temp = temp.next  

# q = LQ()
# q.enqueue(Node(39))
# q.enqueue(Node(94))
# q.enqueue(Node(46))
# q.enqueue(Node(374))
# q.enqueue(Node(35))
# q.enqueue(Node(392))
# q.dequeue()
# q.dequeue()
# q.dequeue()
# q.dequeue()
# q.dequeue()
# q.dequeue()
# q.print()

