## largest among three numbers

## 1st simple method, using if, elif, else
print('#' * 50)
print()
print('This program finds the largest among three numbers.')
print('_' * 30)

x = int(input('x = '))
y = int(input('y = '))
z = int(input('z = '))

print('_' * 30)

def maximum(x, y, z):
	if (x >= y) and (x >= z):
		largest = x
	elif (y >= x) and (y >= z):
		largest = y
	else:
		largest = z		
	return largest

print('The largest number is', maximum(x, y, z))
print()

## 2nd method, using list and max() method
print('#' * 50)
print()
print('This program finds the largest among three numbers.')
print('_' * 30)

x = int(input('x = '))
y = int(input('y = '))
z = int(input('z = '))

print('_' * 30)

def maximum(x, y, z):
	list = [x, y, z]
	return max(list)

print('The largest number is', maximum(x, y, z))
print()


## 3rd method, simply using max() function
print('#' * 50)
print()
print('This program finds the largest among three numbers.')
print('_' * 30)

x = int(input('x = '))
y = int(input('y = '))
z = int(input('z = '))

print('_' * 30)

print('The largest number is', max(x, y, z))
print()


## 4th method, using ternary operator
print('#' * 50)
print()
print('This program finds the largest among three numbers.')
print('_' * 30)

x = int(input('x = '))
y = int(input('y = '))
z = int(input('z = '))

print('_' * 30)

def largest(x, y, z):
    return x if x > y and x > z else y if y > x and y > z else z

print('The largest number is', largest(x, y, z))
print()
