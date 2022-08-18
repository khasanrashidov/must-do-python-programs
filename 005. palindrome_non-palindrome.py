## checking if the entered string is palindrome or non-palindrome
## including any char, symbol, number, text (with spaces)

print('#' * 50)
print()
print('This program checks if the entered string is palindrome or not.')
print('_' * 30)
string = input('String is ')
print('_' * 30)

string.replace(" ", "")

if string == string[::-1]:
    print(string, 'is a palindrome')
else:
    print(string, 'is not a palindrome')
print()
