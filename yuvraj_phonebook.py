#my_phonebook.py
#contact - name,email,phonenumber 
#create contact
#single contact display
#display all contacts
#search contact
#update contact 
#delete contact 
from re import fullmatch

filename = "master_phonebook_list.txt"
def read_file():
	file=open(filename,"r")
	master_data = file.readlines()
	file.close()
	return master_data

def write_data(master_data):
	file = open(filename,"w")
	for j in master_data : 
		file.write(j)
	file.close()

def email_validator(email):
	valid =fullmatch(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)
	if valid:
		return True
	else:
		return False

def contact_validator(con):
	num_len=len(con)
	if num_len>10 or num_len<10:
		return False
	else:
		return True

def email_fun():
	email = input("Enter Contact Email : ")
	r_mail=""
	check=email_validator(email)
	email_is_correct=True
	while email_is_correct:
		if check==True:
			r_mail=email
			email_is_correct=False
		else:
			print("Enter valid Email")
			r_mail=input("Enter email: ")
			ch=email_validator(r_mail)
			if ch==True:
				email_is_correct=False
			else:
				email_is_correct=True
	return r_mail

def contact_fun():
	phone_number = input("Enter Contact Number : ")
	num_check=contact_validator(phone_number)
	con_number_is_correct=True
	while con_number_is_correct:
		if num_check==True:
			r_contact=phone_number
			con_number_is_correct=False
		else:
			print("Enter valid contact number")
			r_contact=input("Enter contact number: ")
			cg=contact_validator(r_contact)
			if cg==False:
				con_number_is_correct=True
			else:
				con_number_is_correct=False
	return r_contact


def create_contact() :
	name = input("Enter Contact Name : ")
	valid_mail=email_fun()
	valid_contact=contact_fun()
	contact_entry = "{},{},{}\n".format(name,valid_mail,valid_contact)
	file = open(filename,"a")
	file.write(contact_entry)
	file.close()

	print("Contact Added Successfully")
"""
Name : Mohit
Email : mohit@gmail.com
Phone Number : 5464353534
"""

def display_contact(x):
	#print(x)
	x = x.replace("\n","")
	#print(x)
	contact = x.split(",")
	#print(contact)
	print("Name : ",contact[0])
	print("Email : ",contact[1])
	print("phone_number : ",contact[2])

def display_all_contact():
	m_data=read_file()
	print("================================")
	for i in m_data: 
		display_contact(i)
		print("================================")
	

def search_contact():
	search_term = input("Enter a Search Term : ")
	m_data=read_file()
	for i in m_data:
		i = i.replace("\n","")
		contact = i.split(",")
		if search_term in contact : 
			print("================================")
			display_contact(i)
			print("================================")
			return i,contact
			break	
	else : 
		print("Contact Not Found ")
		return search_contact()

	

def update_contact():
	current_contact,updated_contact=search_contact()
	current_contact = current_contact + "\n"
	m_data=read_file()
	
	update_choice = input("Press 1 to change Name\nPress 2 to change Email\nPress 3 to Contact Number\nEnter Valid Input : ")
	if update_choice == "1" :
		new_name = input("Enter New Name : ")
		updated_contact[0] = new_name
	elif update_choice == "2":
		updated_contact[1]=email_fun()

	elif update_choice == "3":
		updated_contact[2]=contact_fun()
		
	else :
		print("Invalid Choice")
		return update_contact()


	new_contact = "{},{},{}\n".format(updated_contact[0],updated_contact[1],updated_contact[2])

	current_index = m_data.index(current_contact)
	print("Before Change")
	print(m_data)
	m_data[current_index] = new_contact
	print("After Change")
	print(m_data)

	write_data(m_data)

	print("Contact Updated Successfully")


def delete_contact():
	current_contact,updated_contact=search_contact()
	current_contact = current_contact + "\n"
	m_data=read_file()
	current_index=m_data.index(current_contact)
	m_data.pop(current_index)
	print(m_data)

	write_data(m_data)

	print("Contact successfully deleted!!")
			



