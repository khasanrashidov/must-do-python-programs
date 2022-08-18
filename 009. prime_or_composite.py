##################################################

## prime or composite number

print('#' * 50)
print()
print('This program checks if the entered number is prime or composite.')
print('_' * 30)

num = int(input('Number is '))

## 1st method

## checking if the number is greater than 1
if num > 1:

	## iterating from 2 to num / 2
	for i in range(2, int(num / 2) + 1):
		## if num is divisible by any number between
		## 2 and num / 2, then it is composite (not prime)
		if (num % i) == 0:
			print(num, "is a composite number")
			break
	else:
		print(num, "is a prime number")

else:
	print(num, "is not a prime number")

print('\n' + '#' * 50 + '\n')

##################################################

print('This program checks if the entered number is prime or composite.')
print('_' * 30)

num = int(input('Number is '))

## 2nd method, Optimized Method

from math import sqrt

if num > 1:

	## iterating from 2 to sqrt(num)
	for i in range(2, int(sqrt(num))+1):

		## if num is divisible by any number between
		## 2 and sqrt(num), then it is composite (not prime)
		if (num % i) == 0:
			print(num, "is a composite number")
			break
	else:
		print(num, "is a prime number")

else:
	print(num, "is not a prime number")
print()
##################################################
