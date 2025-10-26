def lower_case(x):
	return x.lower()

def upper_case(x):
	return x.upper()

def sentence_case(x):
	y = ""
	for i in range(len(x)):
		if i == 0 :
			y = x[i].upper()
		elif x[i]=='.':
			pass
		
		else : 
			y = y + x[i].lower()
	return y 

def capitalise_case(x): #what a nice day
	y = x.split(" ") # ["what","a","nice","day"]
	final_result = ""#final result
	for i in y :# i = "a"
		result = "" # intermideate result
		for j in range(len(i)) :
			if j == 0 :
				result = i[j].upper()#"A"
			elif j=='.':
				if j+1==" ":
					continue
				else:
					result = i[j].upper()

			else  : 
				result = result + i[j].lower()
				#result = "A"
		if final_result == "":
			final_result = result # "What A"
		else : 
			final_result = final_result + " " + result 
	return final_result


def toggle_case(x):
	y = x.split(" ")
	final_result = ""
	for i in y :
		result = "" 
		for j in range(len(i)):
			if j == 0 :
				if i[j].isupper():
					result = i[j].lower()
				elif i[j].islower():
					result = i[j].upper()
			else : 
				if i[j].isupper():
					result = result + i[j].lower()
				elif i[j].islower():
					result = result + i[j].upper()

		if final_result == "":
			final_result = result # "What A"
		else : 
			final_result = final_result + " " + result 
	return final_result

 	
def main_function():
	user_str = input("Enter Value : ")
	choice = int(input("Press 1 for Lower Case\nPress 2 for Upper Case\nPress 3 for Sentence Case\nPress 4 for Capitalise Case\nPress 5 for ToggleCase\nPlease Select a Valid Choice : "))
	
	if choice == 1 :
		converted_str = lower_case(user_str)
		print("User String : ",user_str)
		print("After Conversion ")
		print("Converted String : ",converted_str)
		
	
	elif choice == 2 : 
		converted_str = upper_case(user_str)
		print("User String : ",user_str)
		print("After Conversion ")
		print("Converted String : ",converted_str)
		


	elif choice == 3 : 
		converted_str = sentence_case(user_str)
		print("User String : ",user_str)
		print("After Conversion ")
		print("Converted String : ",converted_str)
		
	elif choice == 4 : 
		converted_str = capitalise_case(user_str)
		print("User String : ",user_str)
		print("After Conversion ")
		print("Converted String : ",converted_str)
		
	elif choice == 5 : 
		converted_str = toggle_case(user_str)
		print("User String : ",user_str)
		print("After Conversion ")
		print("Converted String : ",converted_str)
		
	else : 
		print("Invalid Choice selected. Please Re-enter a valid choice ")
		# second_main_function1(user_str)
		act=main_function()
		


exit_program=True

while exit_program:
	main_function()
	user_choice=input("Do you wish to continue type 'Y' for Yes ,'N' for No: ").upper()
	if user_choice=='Y':
		exit_program=True
	else:
		exit_program=False
	



	

	