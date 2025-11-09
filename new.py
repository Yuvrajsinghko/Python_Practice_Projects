# from time import time 


# main_file="fact_file.txt"
# def iterative_fun(n):
	
# 	factorial=1
# 	for i in range(1,n+1):
# 		factorial*=i
	
	

# def fact(n):
	
# 	if n==1 or n==0:
# 		return 1
# 	else:
# 		return n *fact(n-1)
		
	
# for num in range(1,1001):
# 	initial_time1=time()
# 	ans1=iterative_fun(num)
# 	final_time1=time()
# 	initial_time2=time()
# 	ans =fact(num)
# 	final_time2=time()
# 	iterative_time=final_time1-initial_time1
# 	recursive_time=final_time2-initial_time2

# 	final_string=f"Number:{num},value:{ans},iterative_time:{iterative_time},recursive_time:{recursive_time}"
# 	file=open(main_file,"a")
# 	file.write(final_string+"\n")
# 	file.close

import random

all_characters = [
    # Lowercase letters
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z',

    # Uppercase letters
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z',

    # Digits
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',

    # Special characters
    '@', '#', '$'    
]

# test_cases=[]
# user_input=int(input("Enter number of test cases to be generated: "))
# for j in range(user_input+1):
# 	pass_str=""
# 	for i in range(9):
# 		random_index=random.randint(0,len(all_characters)-1)
# 		pass_str+=all_characters[random_index]
# 	if pass_str not in test_cases:
# 		test_cases.append(pass_str)
# 		with open("password.txt",'a') as file:
# 			file.write(pass_str+'\n')
	

# with open("password.txt",'r') as file:
# 	content=file.readlines()
# 	check=[]
# 	for pass_word in content:
# 		pass_word=pass_word.replace("\n",'')
# 		check.append(pass_word)
# ans=set(check)
# def check_list_status(test):
#     min_val=min(test)
#     max_val=max(test)
#
#     def check_asc_order(test):
#         check=0
#         for i in range(len(test)):
#             if i==0 and test[i]==min_val:
#                 check+=1
#             if test[i]<min_val:
#                 check-=1
#             if test[i]>min_val:
#                 check+=1
#         if check==len(test):
#             return True
#         else:
#             return False
#     first_result=check_asc_order(test)
#     print(first_result)
#
# temp=[-1,0,7,9,8,10]
# check_list_status(temp)


prices = [7,1,5,3,6,4]

buying_rate = min(prices)
selling_rate = max(prices)
print(buying_rate,selling_rate)
if prices.index(buying_rate) == prices.index(selling_rate) or prices.index(buying_rate) > prices.index(selling_rate):
    print(0)
elif prices.index(buying_rate) < prices.index(selling_rate):
    print( selling_rate - buying_rate)




















    








	
	