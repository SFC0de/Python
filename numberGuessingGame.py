from random import randint

randomNumber = randint(1,100)
turns = 0

while True:
	guessedNumber = int(input("Please guess a number between 1 and 100: "))
	if guessedNumber > 100 or guessedNumber < 1:
		print("ERROR! Try again.")
		continue
	numberHolder = 0
	
	turns += 1
	if guessedNumber == randomNumber:
		print("You've guessed correctly! Your total number of turns: {}".format(turns))
		break
	elif turns == 1:
		if abs(randomNumber - guessedNumber) <= 10:
			print("Warm!")
			numberHolder = guessedNumber
			continue
		else:
			print("Cold!")
			numberHolder = guessedNumber
			continue
	else:
		if abs(randomNumber - guessedNumber) < abs(randomNumber - numberHolder):
			print("Warmer!")
			numberHolder = guessedNumber
		else:
			print("Colder!")
			numberHolder = guessedNumber