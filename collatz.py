# collatz.py 
# the input number (positvie integer) if even is divided by 2; however if the number is odd it is multiplied by 3 with one added.
# this program ends when the final number reaches 1.
# the program will read back the calculated numbers.
# Author Debi Gormley

inputstring = int(input('Please enter a positive integer:'))

if (inputstring) % 2 == 0:
    print('Your input integer is an even number')
else:
    print('Your input integer is an odd number')
    
while inputstring != 1:
    if inputstring % 2 == 0:
        inputstring /= 2
    else: 
        inputstring = inputstring * 3 + 1
    print (int(inputstring))