# bank.py
#this program allow the user to enter two input amounts of money, the amounts are dded and the total is output in euro and cent"
#Author Debi Gormley

value1 = int(input ("enter amount 1 in cent: "))
value2 = int(input ("enter amount 2 in cent: "))

answer = (value1 + value2) / 100


print (f'The summ of these is: €{answer}' )
