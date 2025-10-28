
def type_cast_str():
	x=input("Enter num: ")
	if x.isnumeric():
		print(int(x))
	else:
		x=float(x)
		b=x%1
		if b==0:
			print(int(x))
		else:
			print(float(x))
	
type_cast_str()

 
def complex_sum():
	a=complex(input("Enter first number: "))
	b=complex(input("Enter first number: "))