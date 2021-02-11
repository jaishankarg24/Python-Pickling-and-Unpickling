import pickle,EmployeeInfo

if __name__ == '__main__':
	try:
		f=open(file='employee.txt', mode='rb')
		print('Unpickling operation started')
		
	except Exception as e:
		print(f'The cause of the exception is : {e.args}')
		
	else:
		print('The Employee Details are:')
		while True:
			try:
				ref=pickle.load(file=f)
				ref.display()
			except EOFError:
				print('Unpickling Completed')
				break

	finally:
		f.close()

# o/p:
# ----
# Unpickling operation started
# The Employee Details are:
# The details of the Employee:
# Name: Sachin
# Address: Mumbai
# Salary: 100000
# The details of the Employee:
# Name: Dravid
# Address: Bangalore
# Salary: 80000
# The details of the Employee:
# Name: Dhoni
# Address: Ranchi
# Salary: 150000
# Unpickling Completed