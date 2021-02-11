import pickle

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
	try:
		with open(file='Student.txt',mode='rb') as f:
			ref=pickle.load(f)
			ref.display()
			print('Unpickling operation Completed...')

	except Exception as e:
		print(f'The cause of the exception is : {e.args}')

# o/p:
# -----
# name:sachin
# age:40
# marks:70
# Unpickling operation Completed...