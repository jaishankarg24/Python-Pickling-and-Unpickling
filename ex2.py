#pickling
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
		f=open(file='Student.txt',mode='wb')
		ref=Student(name='sachin',age=40,marks=70)
		ref.display()
		pickle.dump(obj=ref,file=f)

		print('Student object details is stored in the text file:',f.name)
		print('pickling of Student object is done successfully!!')

	except Exception as e:
		print(f'The cause of the exception is : {e.args}')
	
	finally:   #resource termination
		f.close()
# o/p:
# ----
# name:sachin
# age:40
# marks:70

# Student object details is stored in the text file: Student.txt
# pickling of Student object is done successfully!!