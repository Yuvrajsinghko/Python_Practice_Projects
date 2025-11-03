def uppercase(sentence):
	upper = sentence.upper()
	return (upper) 

def lowercase(sentence):
	lower = sentence.lower()
	return (lower)

def word_capitalise(sentence):
	a = sentence.split()
	b = []

	for i in range(len(a)):
		b = a[i]
		a[i] = b[0].upper() + b[1:].lower()

	capitalise = " ".join(a)
	return(capitalise)

def toggle(sentence):
	a = sentence.split()
	b = []

	for i in range(len(a)):
		b = a[i]
		a[i] = b[0].lower() + b[1:].upper()

	toggle = " ".join(a)
	return(toggle)

def sentence_case(sentence):
	a = sentence.split()
	b = []

	for i in range(len(a)):
		b = a[i]
		a[i] = b[0].upper() + b[1:].lower()

	case = " ".join(a)
	return(case)	

x = str(input("Enter Sentence : "))
y = sentence_case(x)
print(y)