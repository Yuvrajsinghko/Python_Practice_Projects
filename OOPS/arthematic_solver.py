import operator


class stack():
	def __init__(self):
		self.main_stack=[]
		self.max=-1
		self.min=-1

	def status(self):
		print(self.main_stack)
		print(self.max)
		print(self.min)

# valid_chars = set("0123456789+-*/^()")
# stack=[]

# def infix_validater(x):
# 	x=x.replace("",'')
# 	for i,char in enumerate(x):
# 		if char not in valid_chars:
# 			 return(f"Invalid character '{char}' at position {i}")


# 	for i in x:
# 		if i=='(':
# 			stack.append(i)
# 		elif i==')':
# 			if not stack:
# 				return( "Unmatched closing parenthesis")
# 			stack.pop()
# 	if stack:
# 		return( "Unmatched opening parenthesis")

# 	if x[0] in "+-*/^" or x[-1] in "+-*/^":
# 		return("Expression cannot start or end with an operator")

# 	for j in range(len(x)):
# 		if x[j] in "+-*/^":
# 			if x[j+1] in "+-*/^" and j+1<len(x):
# 				return "two operators cannot appear back to back"

# 	if "()" in x:
# 		return "Empty parenthesis are not allowed"	

# 	return x

# class stack():
# 	def push(self,x,char):
# 		x.append(char)
# 	def remove(self,y):
# 		y.pop()

def expression_break():
	expression=input("Enter expression:")
	mix_list=[]
	num=""
	
	for i in range(len(expression)):
		if expression[i]=='-' and i==0:
			num+='-'
		elif expression[i]=='-' and expression[i-1] in "/-+*":
			num+='-'
		elif expression[i].isdigit():
			num=num+expression[i]
		else:
			if num:
				mix_list.append(num)
				num=""
			mix_list.append(expression[i])
	if num:
		mix_list.append(num)
	return mix_list


def infix_validator(op_list):
	if op_list[-1] in "+-*/":
		return False
	if op_list[0] in "/,*,+":
		return False
	else:
		for i in range(len(op_list)):
			if op_list[i] in "+-*/":
				if op_list[i+1] in "+-*/" and i+1<len(op_list):
					return False
		for char in op_list:
			if char.isdigit():
				if int(char)<0:
					return False
	return result

status=infix_validator(result)

def precedence(op):
	if op in "+-":
		return 1
	elif op in "/*":
		return 2


def is_number(char):
    try:
        int(char)  
        return True
    except ValueError:
        return False
	

def infix_to_postfix(x):
	operator_stack=[]
	output=[]
	for char in x:
		if is_number(char):
			output.append(char)
		elif char in "/+*-":
			while(operator_stack and precedence(operator_stack[-1])>=precedence(char)):
				output.append(operator_stack.pop())
			operator_stack.append(char)
	while operator_stack:
		output.append(operator_stack.pop())
	
	return output


def postfix_sol(p):
	operator_dict={'/':operator.truediv,'+':operator.add,'-':operator.sub,'*':operator.mul}
	operand_stack=[]
	for char in p:
		if is_number(char):
			operand_stack.append(char)
		else:
			if char in '/+*-':
				operand_2=int(operand_stack.pop())
				operand_1=int(operand_stack.pop())
				result=(operator_dict[char](operand_1,operand_2))
				operand_stack.append(result)
	final_ans=operand_stack.pop()
	return final_ans
if status:
	result=expression_break()
	print(f"Infix_representation:{result}")
	print("===========================================================")
	conversion=infix_to_postfix(result)
	print(f"Postfix_representation:{conversion}")
	print("===========================================================")
	print(f"Solution of postfix expression:{postfix_sol(conversion)}")


	
















	




			
	




