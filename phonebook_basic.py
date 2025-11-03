"""def initial_phonebook():
	rows = int(input("Enter total no of contacts to be stored : "))
	columns = 3

	Phone_book = []

	for i in range(rows):
		aman = []
		
		for j in range(columns):
			if j == 0:
				aman.append(input("Enter Name : "))

			elif j == 1:
				aman.append(int(input("Enter Contact No : ")))

			elif j == 2:
				aman.append(input("Enter Email : "))

		Phone_book.append(aman)		

	return(Phone_book)

my_phonebook = initial_phonebook()
print(my_phonebook)"""

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
	Name = input("Enter Name: ")
	Number = input("Enter Contact Number: ")
	Email = input("Enter Email Address: ")

	Master_Data_List.append([Name, Number, Email])
	main_file=open("phone_book.txt","w")
	for i in Master_Data_List:
		main_file.write(str(i)+"\n")	
	main_file.close()
	return

def display_contact():
	main_file=open("phone_book.txt","r")
	y = main_file.read()
	for i in y:
		main_file.read(y)
	main_file.close()

	


def search_contact():
	search = input("Enter name to search : ")

	for j in Master_Data_List:
		if j[0].lower() == search.lower():
			print("Name : {}, Number : {}, Email : {}".format(j[0],j[1],j[2]))
			
	else:
		print("Contact not Found")

def update_contact():
	update = input("Enter the contact name to be updated : ")

	for k in Master_Data_List:
		if k[0].lower() == update.lower():
			print("Contact Found.Enter New Details")
			k[0] = input("Enter New Name: ")
			k[1] = input("Enter New Contact Number: ")
			k[2] = input("Enter New Email Address: ")
			print("Contact updated successfully")
			print(Master_Data_List)
			return

	else:
		print("Contact not Found")

def delete_contact():
	delete = input("Enter contact name to be deleted : ")

	for m in Master_Data_List:
		if m[0].lower() == delete.lower():
			Master_Data_List.remove(m)
			print("Contact deleted successfully")
			print(Master_Data_List)
			return
	else:
		print("Contact not found ")



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

