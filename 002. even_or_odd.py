## even or odd

## using if and else
print('#' * 50)
print()
print('This program checks if the entered integer is even or odd.')
print('_' * 30)
number = int(input('Number is '))
print('_' * 30)
if number % 2 == 0:
    print(number, 'is even')
else:
    print(number, 'is odd')

print('_' * 30)

## using ternary operator

print('#' * 50)
print()
print('This program checks if the entered integer is even or odd.')
print('_' * 30)
number = int(input('number is '))
print('_' * 30)

print(number, ('is even' if number % 2 == 0 else 'is odd'))

print('_' * 30)
