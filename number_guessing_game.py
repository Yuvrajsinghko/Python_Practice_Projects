from random import randint


def game_brain():	
	number_of_guesses=0
	game_is_on=True
	random_number=randint(1,20)
	while game_is_on:
		number_of_guesses+=1
		user_input=int(input("Guess the number: "))
		if user_input<=0:
			print("Enter number greater than zero.")

		if number_of_guesses>=5:
			print(f"Better luck next time.Original number was:{random_number}")
			game_is_on=False
			# quit()
		elif user_input==random_number:
			print(f"Correct answer")
			return [f"Number of guesses:{number_of_guesses}",f"Guessed Number:{random_number}"]		
			game_is_on=False
		else:
			
			game_is_on=True
			
	
	
	

ans=game_brain()
print(ans)


