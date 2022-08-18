## fibonacci series

print('#' * 50)
print()
print('This program prints Fibonacci series up to n numbers.')
print('_' * 30)
number = int(input('n = '))
print('_' * 30)

## Fibonacci numbers:
## 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89....


## 1st method, using recursion
## Function for nth Fibonacci number
def fibonacci(n):

        ## Check if input is 0 then it will
        ## print incorrect input
        if n < 0:
                print("Incorrect input")

        ## Check if n is 0
        ## then it will return 0
        elif n == 0:
                return 0

        ## Check if n is 1,2
        ## it will return 1
        elif n == 1 or n == 2:
                return 1

        else:
                return fibonacci(n - 1) + fibonacci(n - 2)

## Driver Program
print(number, '- element of Fibonacci series is', fibonacci(number))


## 2nd method, space optimisation

## Function for nth fibonacci
## number - Space Optimisation
## Taking 1st two fibonacci numbers as 0 and 1

print('#' * 50)
print()
print('This program prints Fibonacci series up to n numbers.')
print('_' * 30)
number = int(input('n = '))
print('_' * 30)


def fibonacci(n):
        a = 0
        b = 1
        
        ## Check is n is less
        ## than 0
        if n < 0:
                print("Incorrect input")
                
        ## Check is n is equal
        ## to 0
        elif n == 0:
                return 0
        
        ## Check if n is equal to 1
        elif n == 1:
                return b
        else:
                print('[0]', 0)
                print('[1]', 1)
                for i in range(1, n):
                        c = a + b
                        a = b
                        b = c
                        print('[{}] {}'.format(i + 1, b))
                return b

## Driver Program
print(number, '- element of Fibonacci series is', fibonacci(number))

print('#' * 50)
print()
