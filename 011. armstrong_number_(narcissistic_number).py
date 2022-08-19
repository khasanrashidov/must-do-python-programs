## Armstrong number (narcissistic number)
##
## Narcissistic number (Armstrong number) is a number
## that is the sum of its own digits
## each raised to the power of the number of digits
## For example,
## number 153 is narcissistic number, because
## 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153;
## other examples are
## 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153,
## 370, 371, 407, 1634, 8208, 9474, 54748, 92727, 93084, 548834, ...


print('#' * 50)
print()
print('This program checks whether the entered number is Armstrong (Narcissistic) number or not.')
print('_' * 30)
number = int(input('Number is '))
print('_' * 30)

number = str(number)

n = len(number)
n = int(n)

total_sum = 0

for digit in number:
    result = int(digit) ** n
    print(result)
    total_sum += result
else:
    print('_' * 30)
    print(total_sum)
    print('_' * 30)

number = int(number)
total_sum = int(total_sum)

if number == total_sum:
    print('{} is a narcissistic number (Armstrong number)'.format(number))
else:
    print('{} is  not a narcissistic number (Armstrong number)'.format(number))
print()
