import random

SecretNumber = random.randint(1,20)

print ('Enter your name to begin')

name = input() 

print ('Well '+ ' ' + name + ' ' + 'i am thinking of number between 1 to 20, to guess it.')
 
for guess in range (1,7):

	UserGuess = int (input())

	if UserGuess < SecretNumber:

		print ('You have guessed too low')
			
	elif UserGuess > SecretNumber:

		print ('You have guessed too high')

	else:

		break 


if SecretNumber == UserGuess:

	print ('Congratulations you have guess the number right in  '  +  str(guess)  + ' '  + 'guess(es)' )

else:

	print ('Unfortunately you could not guess the number right. The number i was thinking was  ' + str(SecretNumber))


