# my_dict={"Name":"Yuvraj Singh",'age':24,'city':'Bhopal'}
# my_dict["Contact No."]=8989404118
# my_dict.pop("Contact No.")
# print(len(my_dict))
# for i,j in my_dict.items():
# 	print(i,j)

master_data_list=[{'Name':"Yuvraj",'Contact_no':8989404118,'E-mail':"yuvraj@gmail.com"},{'Name':'Raj','Contact_no':12345689,'E-mail':"raj@gmail.com"}]

def create_contact():
	name=input("Enter name:")
	cnumber=int(input("Enter number:"))
	emil=input("Enter E-mail:")
	new_dict={'Name':name,'Contact_no':cnumber,'E-mail':emil}
	master_data_list.append(new_dict)
	return (master_data_list)

def display_contact():
	for dic in master_data_list:
		for i,j in dic.items():
			print(i,j)
		print("==========================")

	

def search_contact():
	search_name=input("Enter contact to be searched:")
	result={}
	for names in master_data_list:
		for i in names.values():
			if i==search_name:
				result=names
	return result
				
def user_choice():
	a=int(input("What would you like to update.Press 1 to update name/Press 2 to update contact number/Press 3 to update e-mail"))
	if a==1:
		return 'Name'
	elif a==2:
		return 'Contact_no'
	else:
		return 'E-mail'


def update_contact():
	ch=user_choice()
	for dict_ in master_data_list:
		for key in dict_.keys():
			if ch=='Name' or ch=='E-mail':
				dict_[ch]=input(f"Enter updated {ch}:")
				return master_data_list
			else:
				dict_[ch]=int(input(f"Enter updated {ch}:"))
				return master_data_list

	

def delete_contact():
	na=input("Enter contact to be deleted:")
	for temp_dic in master_data_list:
		for val in temp_dic.values():
			if val ==na:
				master_data_list.remove(temp_dic)
	return master_data_list


print("Welcome to My PhoneBook")
choice = int(input("Press 1 to Add Contact\nPress 2 to Display Contact\nPress 3 to Search Contact\nPress 4 to Update Contact\nPress 5 to Delete Contact\nEnter a Valid Choice : "))

if choice == 1 :
	a=create_contact()
	print(a)
elif choice	== 2 :
	display_contact()
	
elif choice == 3 : 
	a=search_contact()
	print(a)
	
elif choice	== 4 :
	f=update_contact()
	print(f)
elif choice == 5 :
	t=delete_contact()
	print(t)
else :
	print("Invalid Choice Selected. Please reenter a valid choice")