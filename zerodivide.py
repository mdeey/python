def hello (devidezero):
	
	try:
		number = 42 / devidezero
		print (number)
	
	except ZeroDivisionError:
		print ('division by zero is not alllowed !!!!')
hello(12)
hello(2)
hello(0)
hello(1)
	
