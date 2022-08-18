## leap year or not

## Here are the rules of leap years:
## 
## 1) A year may be a leap year if it is evenly divisible by 4.
## 2) Years that are divisible by 100
##    (century years such as 1900 or 2000)
##    cannot be leap years unless
##    they are also divisible by 400.
##    (For this reason, the years 1700, 1800, and 1900 
##    were not leap years, but the years 1600 and 2000 were.)
##
## If a year satisfies both the rules above, then it is a leap year. 


## 1st method
print('#' * 50)
print()
print('This program checks if the entered year is leap or not.')
print('_' * 30)

year = int(input('Year is '))

if year % 100 == 0:
    if year % 400 == 0:
        print('{} is a leap year'.format(year))
    else:
        print('{} is not a leap year'.format(year))
elif year % 4 == 0:
    print('{} is a leap year'.format(year))
else:
    print('{} is not a leap year'.format(year))

print()

## 2nd method
print('#' * 50)
print()
print('This program checks if the entered year is leap or not.')
print('_' * 30)

year = int(input('Year is '))

def checkYear(year):
	if (year % 4) == 0:
		if (year % 100) == 0:
			if (year % 400) == 0:
				return True
			else:
				return False
		else:
			return True
	else:
		return False

if(checkYear(year)):
	print('{} is a leap year'.format(year))
else:
	print('{} is not a leap year'.format(year))
	
print()

## 3rd method
print('#' * 50)
print()
print('This program checks if the entered year is leap or not.')
print('_' * 30)

year = int(input('Year is '))

def checkYear(year):

	## return true if year is a multiple
	## of 4 AND NOT multiple of 100
	## OR year is multiple of 400.
	return (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0));

	
if(checkYear(year)):
	print('{} is a leap year'.format(year))
else:
	print('{} is not a leap year'.format(year))
	
print()

## 4th method, simple method in Python
print('#' * 50)
print()
print('This program checks if the entered year is leap or not.')
print('_' * 30)

year = int(input('Year is '))

def checkYear(year):
	import calendar as c
	return(c.isleap(year))

if(checkYear(year)):
	print('{} is a leap year'.format(year))
else:
	print('{} is not a leap year'.format(year))
	
print()
	
