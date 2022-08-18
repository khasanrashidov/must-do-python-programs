## sum of digits

print('#' * 50)
print()
print('This program calculates the sum of the digits of the number.')
print('_' * 30)
number = int(input('Number is '))
print('_' * 30)

sum_digit = 0
for digit in str(number):
    sum_digit += int(digit)
print('Sum of digits of', number, 'is', sum_digit)

print('_' * 30)
print()

##################################################

## another solution (mathematical approach)
print('#' * 50)
print()
print('This program calculates the sum of the digits of the number.')
print('_' * 30)
number = int(input('Number is '))
print('_' * 30)

n = number

sum_of_digits = 0
for digit in range(number + 1):
    sum_of_digits += number % 10
    number //= 10

print('Sum of digits of', n, 'is', sum_of_digits)

print('_' * 30)
print()

##################################################
