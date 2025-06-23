# Write a one-liner that reverses a string.
Number = int(input("Enter a number: "))
Revers_number = 0
while Number > 0:
    result = int(Number % 10)
    Revers_number = Revers_number * 10 + result
    Number = int(Number / 10)
print("The result is: ", Revers_number)
