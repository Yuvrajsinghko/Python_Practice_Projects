#write a py script to crud of employee and manager in an organization 




class employee : 
	def __init__(self):
		
		self.id = int(input("Enter Id : "))
		self.ename = input("Enter Employee Name : ")
		self.eemail = input("Enter Employee Email : ")
		self.econtact = input("Enter Employee Contact : ")

	def emp_show(self):
		print("Employee Id : ",self.id)
		print("Employee Name : ",self.ename)
		print("Employee Email : ",self.eemail)
		print("Employee Contact : ",self.econtact)

	def emp_update(self):
		con_choice = True
		choice = input("Press 1 to change Name\nPress 2 to change Email\nPress 3 to change Contact\nPlease Enter a valid choice : ")
		while con_choice == True :
			if choice == "1" :
				self.ename = input("Enter New Name : ")
				break
			elif choice == "2" :
				self.eemail = input("Enter New Email : ")
				break
			elif choice == "3" :
				self.econtact = input("Enter New Contact : ")
				break
			else :
				print("Invalid Choice")
				con_choice	= False
		else : 
			print("Employee data updated successfully")
			con_choice	= False
	def emp_delete(self):
		con_choice = True
		choice = input("Press 1 to delete Name\nPress 2 to delete Email\nPress 3 to delete Contact\nPlease Enter a valid choice : ")
		while con_choice == True :
			if choice == "1" :
				self.ename = "NA"
				break
			elif choice == "2" :
				self.eemail = "NA"
				break
			elif choice == "3" :
				self.econtact = "NA"
				break
			else :
				print("Invalid Choice")
				con_choice	= True
		else : 
			print("Employee data deleted successfully")
			con_choice	= False


"""
class person:
	def random(self) :
		print("Hi")"""

class manager(employee):
	def __init__(self):
		super(manager, self).__init__()
		self.edepartment = input("Enter Department : ")

	def manager_show(self):
		super().emp_show()
		print("Department : ",self.edepartment)
		
	def manager_update(self):
		choice = input("Press 1 to update Name\nPress 2 to update Email\nPress 3 to update Contact\nPress 4 to update Contact\nPlease Enter a valid choice : ")
		if choice == "1" :
			self.ename = input("Enter New Name : ")			
		elif choice == "2" :
			self.eemail = input("Enter New Email : ")			
		elif choice == "3" :
			self.econtact = input("Enter New Contact : ")			
		elif choice=='4':
			self.edepartment=input("Enter new department name:")
		else :
			print("Invalid Choice")
	def manager_delete(self):
		self.choice = input("Press 1 to update Name\nPress 2 to update Email\nPress 3 to update Contact\nPress 4 to update Contact\nPlease Enter a valid choice : ")
		if choice == "1" :
			self.ename = 'NA'
			
		elif choice == "2" :
			self.eemail = "NA"
			
		elif choice == "3" :
			self.econtact = "NA"
			
		elif choice=='4':
			self.edepartment="NA"
		else :
			print("Invalid Choice")



#E1 = employee()
#E1.emp_show()
#E1.emp_update()
#E1.emp_show()

M1 = manager()
print("================")
M1.manager_show()
print("================")
M1.manager_update()
print("================")
M1.manager_show()
