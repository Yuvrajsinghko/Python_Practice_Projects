""" 
class complex:
	def __init__(self,real,img):
		self.real = real
		self.img = img 

	def show(self):
		if self.img < 0 : 
			print("{}{}i".format(self.real,self.img))
		else : 
			print("{}+{}i".format(self.real,self.img))

	def __add__(self,other):
		x = self.real + other.real  
		y = self.img + other.img
		return complex(x,y)

c1 = complex(1,2)
c1.show()

c2 = complex(2,-4)
c2.show()

#c3 = c1 + c2 
c3 = c1.__add__(c2)

c3.show()
"""
	
class complex:
	def __init__(self, a = None,b = None):
		if a == None and b == None :
			self.real = int(input("Enter Real Part : "))
			self.img = int(input("Enter Imginary Part : "))
		else :
			self.real = a
			self.img = b

	def show(self):
		if self.img < 0 : 
			print("{}-{}i".format(self.real,self.img))
		else : 
			print("{}+{}i".format(self.real,self.img))

	def __add__(self,other):
		x = self.real + other.real  
		y = self.img + other.img
		return complex(x,y)

c1 = complex()
c1.show()

c2 = complex()
c2.show()

#c3 = c1 + c2 
c3 = c1.__add__(c2)

c3.show()