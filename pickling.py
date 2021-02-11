import pickle,EmployeeInfo

if __name__ == '__main__':
	try:
		f=open(file='employee.txt', mode='wb')
		number=int(input('Enter the number of Employees:\t'))
		for i in range(number):
			name=input('Enter the name of the Employee:\t')
			address=input('Enter the address of the Employee:\t')
			salary=int(input('Enter the salary of the Employee:\t'))
			ref=EmployeeInfo.Employee(name=name,address=address,salary=salary)
			pickle.dump(obj=ref, file=f)
	except Exception as e:
		print(f'The cause of the exception is : {e.args}')
	else:
		print('pickling operation successfully completed')
	finally:
		f.close()

# o/p:
# ----
# Enter the number of Employees:	3
# Enter the name of the Employee:	Sachin
# Enter the address of the Employee:	Mumbai
# Enter the salary of the Employee:	100000
# Enter the name of the Employee:	Dravid
# Enter the address of the Employee:	Bangalore
# Enter the salary of the Employee:	80000
# Enter the name of the Employee:	Dhoni
# Enter the address of the Employee:	Ranchi
# Enter the salary of the Employee:	150000
# pickling operation successfully completed