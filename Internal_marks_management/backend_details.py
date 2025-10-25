
st_file="student_record.txt"

def read_fi():
	file=open(st_file,"r")
	student_details = file.readlines()
	file.close()
	return student_details




def create_st_id():
	st_name=input("Enter name of the student:")
	st_rollnum=input("Enter roll number:")
	course_name=input("Enter course name:")
	fin_st_rec=f"{st_name},{st_rollnum},{course_name}\n"
	file=open(st_file,"a")
	file.write(fin_st_rec)
	file.close()

	print("Successfully Registered")




def show_details(x):
	x=x.replace("\n",'')
	details=x.split(',')
	print("Name : ",details[0])
	print("Student Rollnum : ",details[1])
	print("Course Name : ",details[2])
	

def show_single_st_detail():
	search_term = input("Enter Student Name: ")
	st_detail=read_fi()
	
	for line in st_detail:
		line=line.replace('\n','')
		fin=line.split(',')
		if search_term in fin:
			print("=========================================")
			show_details(line)
			print("=========================================")
			return line,fin			
	else:
		print("Enter valid student Name:")
			




def show_all_st_details():
	st_data=read_fi()
	
	print("==========================")
	for i in range(len(st_data)):
		a=st_data[i]
		show_details(a)
		print("========================")

	

def update_st_record():
	current_s_detail,updated_st_detail=show_single_st_detail()
	current_s_detail=current_s_detail+'\n'

	data_st=read_fi()
	ch=int(input("Press 1 to update name of the student\nPress 2 to update rollnumber\nPress 3 to update course name "))
	if ch==1:	
		name=input("Enter updated name: ")
		updated_st_detail[0]=name
	elif ch==2:
		roll=input("Enter updated rollnumber: ")
		updated_st_detail[1]=roll
	elif ch==3:
		course=input("Enter updated course: ")
		updated_st_detail[2]=course	

	finale_st_detail=f"{updated_st_detail[0]},{updated_st_detail[1]},{updated_st_detail[2]}\n"
	print(current_s_detail)
	curr_index=data_st.index(current_s_detail)
	print("Before Change")
	print(data_st)
	data_st[curr_index]=finale_st_detail
	print("After change")
	print(data_st)
	file=open(st_file,"w")
	for i in data_st:
		file.write(i)
	file.close()
	return updated_st_detail

def delet_st_record():
	current_s_detail,updated_st_detail=show_single_st_detail()
	current_s_detail+='\n'

	student_data=read_fi()
	
	current_index=student_data.index(current_s_detail)
	student_data.pop(current_index)
	file=open(st_file,"w")
	for j in student_data:
		file.write(j)
	file.close()

	print("deleted successfully")

