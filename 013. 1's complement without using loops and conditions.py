## Computing one's complement without using
## conditions and loop.
b_num = str(input("Input is ")) ## entered 'number' is just a text

len_bin = len(b_num)            ## saving the length of entered number

b_num = str('1' + b_num)        ## now it is a '1number', we add '1' in the beginning of the text

ones = len(b_num)               ## remembering the length of '1number'

b_num = int(b_num)              ## now '1number' is integer

ones = int('1' * ones)          ## we have as much '1's as the length of '1number'

b_num = ones - b_num            ## subtracting '1number' from '1's

b_num = str(b_num)              ## converting the number to text again

## So, then we are printing the output aligned to the right
## according to the length it was entered before,
## in case length it not the same, it will be filled with zeros.

output = 'Output is {0:0>{1}}'.format(b_num, len_bin)

print(output)

## this DM program was written in python

'''
pseudocode

b_num = str(input("Input is "))

b_num = str('1' + b_num)      

ones = length of b_num            

b_num = converting b_num to integer              

ones = int(multiplying text '1' by length of b_num)    

b_num = ones - b_num 

'''
