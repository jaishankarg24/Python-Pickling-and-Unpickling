#NON Persistent object/temporary object

class Student:
	def __init__(self,name,age,marks): #constructor
		self.name=name
		self.age=age
		self.marks=marks
	def display(self):               #instance method
		print(f'name:{self.name}')
		print(f'age:{self.age}')
		print(f'marks:{self.marks}')

if __name__ == '__main__':
	ref=Student(name='sachin',age=40,marks=70)
	ref.display()
