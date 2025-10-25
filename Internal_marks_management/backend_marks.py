from backend_details import *


sub1="subject_1_marks.txt"
sub2="subject_2_marks.txt"
final_m="final_marksheet.txt"
def sub1_read():
	file=open(sub1,"r")
	sub_data=file.readlines()
	return sub_data
	file.close()

def sub2_read():
	file=open(sub2,"r")
	sub_data=file.readlines()
	return sub_data
	file.close()



def show_marks(x):
	x=x.replace("\n",'')
	det=x.split(',')
	print("Name: ",det[0])
	print("First Internal: ",det[1])
	print("Second Internal: ",det[2])
	print("Third Internal: ",det[3])
	print("Total out of 40:",det[4])
	
	

def search_st(x,search_term):
	st_sub1_data=x()
	for lin in st_sub1_data:
		lin=lin.replace('\n','')
		fin=lin.split(',')
		if search_term in fin:
			print("=========================================")
			show_marks(lin)
			print("=========================================")
			return lin,fin			
	else:
		print("Enter valid student Name:")

def write_marks(master_data,x):
	file = open(x,"w")
	for j in master_data : 
		file.write(j)
	file.close()

def show_single_st_details(x):
	
	st_detail=read_fi()
	
	for line in st_detail:
		line=line.replace('\n','')
		fin=line.split(',')
		if x in fin:
			print("=========================================")
			show_details(line)
			print("=========================================")
			return line,fin			
	else:
		print("Enter valid student Name:")



def enter_marks():
	choice=int(input("Which subject marks do you wish to enter.\nPress 1 for subject-1\nPress 2 for subject-2: "))
	
	
	if choice==1:
		sub1_final_marks=0
		file1=open(sub1,"a")
		sub="subject-1"
		print("You are entering marks for subject-1 currently")
		name=input("Enter name of student:")
		internal_1=int(input("Enter internal 1 marks:"))
		internal_2=int(input("Enter internal 2 marks:"))
		internal_3=int(input("Enter internal 3 marks:"))
		inter_marks_list=[internal_1,internal_2,internal_3]
		inter_marks_list.sort(reverse=True)
		sub1_sum=inter_marks_list[0]+inter_marks_list[1]
		sub1_final_marks+=sub1_sum
		fin_marks=f"{name},{internal_1},{internal_2},{internal_3},{sub1_final_marks}\n"
		file1.write(fin_marks)
		file1.close()
		
	else:
		file1=open(sub2,"a")
		sub_2="subject-2"
		sub2_final_marks=0
		print("You are entering marks for subject-2 currently")
		name=input("Enter name of student:")
		s2_internal1=int(input("Enter internal 1 marks:"))
		s2_internal2=int(input("Enter internal 2 marks:"))
		s2_internal3=int(input("Enter internal 3 marks:"))
		s2_internal_marks_list=[s2_internal1,s2_internal2,s2_internal3]
		s2_internal_marks_list.sort(reverse=True)
		sub2_sum=s2_internal_marks_list[0]+s2_internal_marks_list[1]
		sub2_final_marks+=sub2_sum
		s2_marks=f"{name},{s2_internal1},{s2_internal2},{s2_internal3},{sub2_final_marks}\n"
		file1.write(s2_marks)
		file1.close()
		

def show_single_st_detail():
	subject_ch=int(input("Enter which subject marks you want to display.Press 1 for sub-1,Press 2 for sub-2,Press 3 for both: "))
	search_term = input("Enter Student Name: ")

	st_sub1_data=sub1_read()
	st_sub2_data=sub2_read()
	if subject_ch==1:
		for lin in st_sub1_data:
			lin=lin.replace('\n','')
			fin=lin.split(',')
			if search_term in fin:
				print("=========================================")
				show_marks(lin)
				print("=========================================")				
			else:
				print("Enter valid student Name:")
	elif subject_ch==2:
		for los in st_sub2_data:
			los=los.replace('\n','')
			fin=los.split(',')
			if search_term in fin:
				print("=========================================")
				show_marks(los)
				print("=========================================")
							
		else:
			print("Enter valid student Name:")
	else:
		print("Subject-1 Marks")
		for marks_detail1 in st_sub1_data:
			marks_detail1=marks_detail1.replace('\n','')
			fin=marks_detail1.split(',')
			if search_term in fin:
				print("=========================================")
				show_marks(marks_detail1)
				print("=========================================")
		print("subject-2 Marks")
		for marks_detail2 in st_sub2_data:
			marks_detail2=marks_detail2.replace('\n','')
			fin=marks_detail2.split(',')
			if search_term in fin:
				print("=========================================")
				show_marks(marks_detail2)
				print("=========================================")
					

def show_all_marks():
	pass
def show_st_marks():
	pass
def delet_st_record():
	search_name=input("Enter name of the student: ")
	current_detail1,a=search_st(sub1_read,search_name)
	current_detail2,b=search_st(sub2_read,search_name)
	current_detail3,c=show_single_st_details(search_name)
	current_detail1=current_detail1 + "\n"
	current_detail2=current_detail2 + "\n"
	current_detail3=current_detail3 + "\n"
	data1=sub1_read()
	data2=sub2_read()
	data3=read_fi()
	current_index1=data1.index(current_detail1)
	data1.pop(current_index1)
	print(data1)
	current_index2=data2.index(current_detail2)
	data2.pop(current_index2)
	print(data2)
	current_index3=data3.index(current_detail3)
	data3.pop(current_index3)
	print(data3)
	write_marks(data1,sub1)
	write_marks(data2,sub2)
	write_marks(data3,st_file)
	print("Student record deleted successfully")

def update_marks():
	datas1=sub1_read()
	datas2=sub2_read()
	updated_det=[]
	cho=int(input("What would you like to update.Press 1 to update student details.Press 2 to update marks."))
	if cho==1:
		updated_det+=update_st_record()
	else:	
		io=int(input("Enter which subject marks you want to update.\nPress 1 for first subject\nPress 2 for second subject:"))
		ser_name=input("Enter name of the student:")
		if io==1:
			ans=int(input("Enter which internal marks you want to update.\nPress 1 for first internal\nPress 2 for second internal\nPress 3 for third internal"))
			a,sub1_d=search_st(sub1_read,ser_name)
			sub1_d[1]=int(sub1_d[1])
			sub1_d[2]=int(sub1_d[2])
			sub1_d[3]=int(sub1_d[3])
			
			if ans==1:
				in_1=int(input("Enter new first internal marks: "))
				sub1_d[1]=in_1
			elif ans==2:
				in_2=int(input("Enter new second internal marks: "))
				sub1_d[2]=in_2
			else:
				in_3=int(input("Enter new third internal marks: "))
				sub1_d[3]=in_3
			inter_marks_list=[sub1_d[1],sub1_d[2],sub1_d[3]]
			print(inter_marks_list)
			inter_marks_list.sort(reverse=True)
			sub1_sum=inter_marks_list[0]+inter_marks_list[1]
			# sub1_final_marks+=sub1_sum
			fin_string=f"{sub1[0]},{sub1_d[1]},{sub1_d[2]},{sub1_d[3]},{sub1_sum}"
			c_index=datas1.index(a)
			print("Before Change")
			print(datas1)
			datas1[c_index]=fin_string
			print("After Change")
			print(datas1)
			write_marks(datas1,sub1)
			print("Subject-1 Marks have been updated successfully")
		else:
			ans=int(input("Enter which internal marks you want to update.\nPress 1 for first internal\nPress 2 for second internal\nPress 3 for third internal"))
			a,sub2_d=search_st(sub2_read,ser_name)
			sub2_d[1]=int(sub2_d[1])
			sub2_d[2]=int(sub2_d[2])
			sub2_d[3]=int(sub2_d[3])
			if ans==1:
				in_1=int(input("Enter new first internal marks: "))
				sub2_d[1]=in_1
			elif ans==2:
				in_2=int(input("Enter new second internal marks: "))
				sub2_d[2]=in_2
			else:
				in_3=int(input("Enter new third internal marks: "))
				sub2_d[3]=in_3
			inter_marks_s2=[sub2_d[1],sub2_d[2],sub2_d[3]]
			inter_marks_s2.sort(reverse=True)
			sub1_sum=inter_marks_s2[0]+inter_marks_s2[1]
			# sub1_final_marks+=sub1_sum
			s2_string=f"{sub1[0]},{sub2_d[1]},{sub2_d[2]},{sub2_d[3]},{sub1_sum}"
			s2_index=datas1.index(a)
			print("Before Change")
			print(datas1)
			datas2[s2_index]=s2_string
			print("After Change")
			print(datas2)
			write_marks(datas2,sub2)
			print("Subject-2 Marks have been updated successfully")








			






	






	


