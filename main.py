import random

while True: 
	print('Make your move:')
	choice = str(input())
	choice = choice.lower()

	print("You chose", choice)

	choices = ['rock', 'paper', 'scissors']

	computer_choice = random.choice(choices)

	print("Computer choice is", computer_choice)
	if choice in choices:
		if choice == computer_choice:
			print('It\'s a tie ')
		if choice == 'rock':
			if computer_choice == 'paper':
				print('Aw ... You lost')
			elif computer_choice == 'scissors':
				print('Victory')
		if choice == 'paper':
			if computer_choice == 'scissors':
				print('ha ha ha!')
			elif computer_choice == 'rock':
				print('Good Job!')
		if choice == 'scissors':
			if computer_choice == 'rock':
				print('Get lost')
			elif computer_choice == 'paper':
				print('Nice Strategy!')
	else:
		print('Invalid Choice')
