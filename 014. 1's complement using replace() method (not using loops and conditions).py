## Computing one's complement without using
## conditions and loop.
## Using replace() method.
b_num = str(input("Input is "))

b_num = b_num.replace('1', '2')

b_num = b_num.replace('0', '1')

b_num = b_num.replace('2', '0')

print("Output is", b_num)

'''

pseudocode

b_num = str(input("Input is "))

b_num = is replacing all ones with twos

b_num = is replacing all zeros with ones

b_num = is replacing all twos with zeros

print("Output is", b_num)

'''
