from email_ob import *

def main():
	user_input=input("What would like to display.\nPress 1 to display original file.\nPress 2 to display obfuscated version of original file.\nPress 3 to display deobfuscated version of original file.\nEnter valid choice: ")
	if user_input=='1':
		for i in a_data:
			print(i+'\n')
	elif user_input=='2':
		for j in c_data:
			print(j+'\n')
	elif user_input=='3':
		d_file=open("D.txt",'r')
		d_data=d_file.readlines()
		for k in d_data:
			print(k+'\n')
		d_file.close()
	else:
		main()



to_continue=True
while to_continue:	
	if to_continue==True:
		main()
		choice=input("Do you wish to continue.Press 'Y' for Yes,'N' for No: ").upper()
		if choice=='Y':
			to_continue=True
		else:
			to_continue=False
	

