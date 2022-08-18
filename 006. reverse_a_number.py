## reverse a number

## simple approach
print('#' * 50)
print()
print('This program reverses a number (i. e. reverses its digits).')
print('_' * 30)
number = int(input('Number is '))
print('_' * 30)

number = str(number)
number = number[::-1]
number = int(number)

print(number)

print()

## mathematical approach to reverse a number
print('#' * 50)
print()
print('This program reverses a number (i. e. reverses its digits).')
print('_' * 30)
n = int(input('Number is '))
print('_' * 30)

rev = 0

while(n > 0):
	a = n % 10; print(a)
	rev = rev * 10 + a; print(rev)
	n = n // 10; print(n)

print("reversed number is", rev)

print()
