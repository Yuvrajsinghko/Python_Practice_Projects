import string
from random import random, randint,shuffle


# mainfile="User_id.txt"    
  

# def random_user_id(x,y):
# 	final_list=list(string.digits)+list(string.ascii_letters)+list(string.punctuation)
	
# 	for i in range(x):
# 		user_id=""
# 		for j in range(y):
# 			rand=randint(0,len(final_list)-1)
# 			let=final_list[rand]
# 			user_id+=let
# 		print(user_id)
		
		
	
	
	


# random_user_id(4,6)

def rgb_color_gen():
	a=randint(0,255)
	b=randint(0,255)
	c=randint(0,255)
	return(f"rgb({a},{b},{c})")
rgb_color_gen()



# list_of_rgb_colors()
def shuffle_list(x):
	final_list=[]
	for i in range(len(x)):		
		index=randint(0,len(x)-1)
		a=x[i]
		final_list.insert(index,a)
		
	return final_list

def  list_of_hexa_colors():
	a=list(string.digits)
	b=list(string.ascii_letters)
	let=b[0:6]
	# choice_list=[]
	choice_list=let+a
	jumbled_list=shuffle_list(choice_list)
	hexa_code="#"
	for i in range(7):
		ch=jumbled_list[i]
		hexa_code+=ch
	return hexa_code


# def list_of_colors_codes():
# 	t=int(input("Enter range  rgb  or hexa colors to be displayed:"))
# 	choice=int(input("Enter number of  rgb  or hexa colors to be displayed.\nPress 1 for rgb\n2 for hexa"))

# 	rgb_list=[]
# 	hexa_color=[]
# 	for i in range(t):
# 		ans=rgb_color_gen()
# 		rgb_list.append(ans)
# 		cd=list_of_hexa_colors()
# 		hexa_color.append(cd)

# 	if choice==1:
# 		return f"rgb:{rgb_list}"	
# 	else:
# 		return f"Hexa:{hexa_color}"	
					
# an=list_of_colors_codes()
# print(an)
	
def rand_num_list():
	num_list=[]
	
	numbers=[0,1,2,3,4,5,6,7,8,9]
	shuffle(numbers)
	for f in range(7):
		num=numbers[f]
		num_list.append(num)			
	return num_list
	
		



result=rand_num_list()
print(result)

















