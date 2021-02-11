class Employee:
	def __init__(self,name,address,salary): #creation of state of objects
		self.name=name
		self.address=address
		self.salary=salary

	def display(self):
		print('The details of the Employee:')
		print(f'Name: {self.name}')
		print(f'Address: {self.address}')
		print(f'Salary: {self.salary}')