## swapping two numbers
## we have several ways to swap numbers in python

## 1st method
print('#' * 50)
print()
print('This program swaps two entered numbers.')
print('_' * 30)
a = int(input('a = '))
b = int(input('b = '))
print('_' * 30)
print('a =', a)
print('b =', b)  
a, b = b, a
print('_' * 30)
print('a and b are swapped')
print('_' * 30)  
print('a =', a)
print('b =', b)
print('_' * 30)

## 2nd method
print('#' * 50)
print()
print('This program swaps two entered numbers.')
print('_' * 30)
a = int(input('a = '))
b = int(input('b = '))
print('_' * 30)
print('a =', a)
print('b =', b)
a = a + b
b = a - b
a = a - b
print('_' * 30)
print('a and b are swapped')
print('_' * 30)  
print('a =', a)
print('b =', b)
print('_' * 30)

## 3rd method
print('#' * 50)
print()
print('This program swaps two entered numbers.')
print('_' * 30)
a = int(input('a = '))
b = int(input('b = '))
print('_' * 30)
print('a =', a)
print('b =', b)
a = a * b
b = a / b ## division returns float number
a = a / b ## division returns a number type of float
print('_' * 30)
print('a and b are swapped')
print('_' * 30)  
print('a =', a)
print('b =', b)
print('_' * 30)
