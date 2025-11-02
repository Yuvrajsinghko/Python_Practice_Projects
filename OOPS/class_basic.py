class contact:
	def __init__(self):
		self.name = input("Enter Name : ")
		self.email = input("Enter Email : ")
		self.phone = input("Enter Phone : ")

	def show(self):
		print("============================")
		print("Contact Name : ",self.name)
		print("Contact Email : ",self.email)
		print("Contact Phone : ",self.phone)
		print("============================")

	def update(self):
		choice = input("Press 1 to Change Name\nPress 2 to Change Email\nPress 3 to Change Phone No.\nEnter a valid Choice : ")
		if choice == "1":
			self.name = input("Enter New Name : ")
		elif choice == "2":
			self.email = input("Enter New Email : ")
		elif choice == "3":
			self.phone = input("Enter New Phone : ")
		else : 
			print("Invalid Choice")

	def delete(self):
		choice=input("Press 1 to Delete Name\nPress 2 to Delete Email\nPress 3 to Delete Phone No.\nEnter a valid Choice : ")
		if choice == "1":
			self.name ="NA"
		elif choice == "2":
			self.email ="NA"
		elif choice == "3":
			self.phone ="NA"
		else : 
			print("Invalid Choice")

	def write_details(self):
		input_str=f"{self.name},{self.email},{self.phone}\n"	
		with open("contact_details.txt",'a') as confile2:
			confile2.write(input_str)




