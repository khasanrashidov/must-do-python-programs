## factorial of a number

## using recursion

def factorial(number):
    if number == 1 or number == 0:
        return 1
    else:
        return (number * factorial(number - 1))

print('#' * 50)
print()
print('This program calculates the factorial of a number.')
print('_' * 30)
number = int(input('Number is '))
print('_' * 30)
print('The factorial of', number, 'is', factorial(number))

## using using for loop

print('#' * 50)
print()
print('This program calculates the factorial of a number.')
print('_' * 30)

number = int(input('Number is '))

factorial = 1

for n in range(1, number + 1):
    factorial *= n

print('_' * 30)
print('The factorial of', n, 'is', factorial)

## using using while loop

print('#' * 50)
print()
print('This program calculates the factorial of a number.')
print('_' * 30)

number = int(input('Number is '))
n = number
factorial = 1

if number < 0:
    print("Factorial does not defined for negative integer.");
elif(number == 0):
    print("The factorial of 0 is 1");
else:
    while number > 0:
        factorial *= number
        number -= 1

print('_' * 30)
print('The factorial of', n, 'is', factorial)

# Python code to demonstrate math.factorial()

print('#' * 50)
print()
print('This program calculates the factorial of a number.')
print('_' * 30)

number = int(input('Number is '))

import math
print ("The factorial of", number, "is ", end="")
print (math.factorial(number))
