
# while1.py

money = 1000
transfer = 1000000

print('Check:', money < transfer)

while money < transfer:
	print('Please enter the amount of money')
	transfer = int(input('new transfer: '))
	if transfer > 1000000:
		print('You do not have enough money to transfer. Please enter a smaller number')
		break

print('You have successfully transfer your money')