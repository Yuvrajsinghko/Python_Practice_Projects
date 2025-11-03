#write py script to make a phonebook which contains the contact details where 
# each contact contains Name, Contact Number and Email Address. And the phonebook can 
# perform the following functions 
#1. Create a Contact
#2. Display a Contact
#3. Search a Contact
#4. Update a Contact 
#5. Delete a Contact

Master_Data_List = [["Aman",987654321234,"qwert@gamil.com"],["Yuvraj",9876564443,"yuvraj"]]

def create_contact():
	pass

def display_contact():
	pass

def search_contact():
	pass

def update_contact():
	pass

def delete_contact():
	cid=input("Enter contact to be deleted: ")
	for i in Master_Data_List:
		if cid in i:
			mid=Master_Data_List.index(i)
			del_id=Master_Data_List.pop(mid)

			


	
	print(Master_Data_List)




print("Welcome to My PhoneBook")
choice = int(input("Press 1 to Add Contact\nPress 2 to Display Contact\nPress 3 to Search Contact\nPress 4 to Update Contact\nPress 5 to Delete Contact\nPlease Enter a Valid Choice : "))
if choice == 1 :
	create_contact()
elif choice	== 2 :
	display_contact()
elif choice == 3 : 
	search_contact()
elif choice	== 4 :
	update_contact()
elif choice == 5 :
	delete_contact()
else :
	print("Invalid Choice Selected. Please reenter a valid choice")
