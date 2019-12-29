import random

random_number = random.randint(1,10)

while True:
	guess = int(input("Guess a number: "))
	if guess < random_number:
		print("You guessed too low")
	
	elif guess > random_number:
		print("You guessed too high")
	else:
		print("You WIN")
		response = input("Would you like to play again? (y/n) ")
		if response == 'y':
			random_number = random.randint(1,10)
			guess = None
		else:
			print("Thanks for playing!")
			break


