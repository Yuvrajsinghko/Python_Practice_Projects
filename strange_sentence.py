
def upper_case(sen):
	a=sen.upper()
	print(a)


def lower_case(x):
	b=x.lower()
	print(b)


def cap_each_word(y):
	a=y.split(" ")
	
	for i in range(len(a)):
		b=a[i]
		a[i]=b[0].upper()+b[1:].lower()
		cap=" ".join(a)


	print(cap)


def sentence_case(z):
	
	ans=z[0].upper()
	new_string=ans+z[1:]
	print(new_string)




def toggle_case(m):
	finale_sentence=""
	for letter in m:
		if letter.isupper():
			st=letter.lower()
			finale_sentence+=st
		elif letter.islower():
			u=letter.upper()
			finale_sentence+=u
		elif letter==" ":
			finale_sentence+=" "
	print(finale_sentence)




print("Welcome to Strange sentence creation")
user_input=input("Enter a sentence:")
choice = int(input("Press 1 to Upper case\nPress 2 to Lower case\nPress 3 to Captilize each word\nPress 4 to Sentence case\nPress 5 to Toggle Case: "))
if choice == 1 :
	upper_case(user_input)
elif choice	== 2 :
	lower_case(user_input)
elif choice == 3 : 
	cap_each_word(user_input)
elif choice	== 4 :
	sentence_case(user_input)
elif choice == 5 :
	toggle_case(user_input)
else :
	print("Invalid Choice Selected. Please re-enter a valid choice")

