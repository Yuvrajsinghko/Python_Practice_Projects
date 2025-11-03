from yuvraj_phonebook import *



def main_fun():
	print("Welcome to My Phonebook Project")
	choice = input("Press 1 for Creating contact\nPress 2 for Display All Contact\nPress 3 Search Contact\nPress 4 for Update Contact\nPress 5 for Delete Contact\nPlease Enter a Valid Choice : ")
	if choice == "1" :
		create_contact()
	elif choice == "2" :
		display_all_contact()
	elif choice == "3":
		search_contact()
	elif choice == "4" :
		update_contact()
	elif choice == "5":
		delete_contact()
	else : 
		print("Invalid Choice, Please enter a valid choice ")
		main_fun()


exit_phonebook=True
while exit_phonebook:
	main_fun()
	user_input=input("Do you wish to continue.Press 'Y'for Yes,'N' for No:").upper()
	if user_input=='Y':
		exit_phonebook=True
	else:
		exit_phonebook=False
