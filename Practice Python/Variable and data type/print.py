print("Hello, world")

print(type(52)) #What is the output of print(type(42))

# Create a variable name and assign your name to it. Print it.
variable = "Johan liebert" 
print(variable)

# Get two numbers from the user and print their sum.
num1 = input("Enter the number ")
num2 = input("Enter the second number ")
print("The result is: ", int(num1) + int(num2))

# What is the difference between `=` and `==`?
a = 45
b = 48
print(a == b)

 #Find the type of variable: `a = "123"`, `b = 123`, `c = 123.0`.
a = "123"
b = 123
c = 123.0
print(type(a))
print(type(b))
print(type(c))

# Convert a string `"56"` into an integer and print the result.
string = "56"
print(int(string))

# Print the result of `3**2 + 4*5 - 6/3`.
print("The result is: ", 3**2 + 4*5 - 6/3)

# Swap two numbers without using a third variable.
ver1 = 19
ver2 = 45
ver3 = ver1
ver1 = ver2
ver2 = ver3
print("After swapping: ")
print("ver1 = ", ver1)
print("ver2 = ",ver2)

# Write a program to calculate area of a rectangle.
Base = float(input("Enter the base: "))
Hight = float(input("Enter the hight: "))
Area = ((1/2) * Base * Hight )
print(Area)

#Accept user's name and age, then print "Hi NAME, you are AGE years old."
name = "JOHAN LIEBERT,"
age = 18
print("Hi",name,"you are",age,"years old.") 

# Write a program to check if a number is even or odd.
number = int(input('Enter the number: '))
result = number % 2 
if result == 0:
    print("The number is even")
if result != 0:
    print("The number is odd")

# What happens if you divide an integer by zero?
integer = int(input("Enter a integer: "))
integer /= 0
print("After dividing by zero the result is:",integer)