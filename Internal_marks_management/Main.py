from backend_details import *
from backend_marks import *
print("WELCOME TO INTERNAL MARKS MANAGEMENT")

user_choice=int(input("Press 1 to add student info and marks\nPress 2 to show student marks\nPress 3 to update student record\nPress 4 to delet student record\nPress 5 to show final marksheet: "))


if user_choice==1:
	t=int(input("Press 1 to enter new student.Press 2 to enter marks: "))
	if t==1:
		create_st_id()
	else:
		enter_marks()
			
elif user_choice==2:
	choice=int(input("Press 1 to show all student marks\nPress 2 to show specific student marks: "))
	if choice==1:
		pass
		show_all_st_details()
		# show_all_marks()
	else:
		show_single_st_detail()
		# show_st_marks()	
	
elif user_choice==3:
	a=print("Ehat would you like to update student details or Marks.Press 1 for updating student details\nPress 2 for updating marks")
	if a==1:
		pass
	else:
		update_marks()

	
	
elif user_choice==4:
	delet_st_record()

elif user_choice==5:
	show_st_marksheet()






