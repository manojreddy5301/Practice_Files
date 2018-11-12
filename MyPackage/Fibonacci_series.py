def calc_fibonacci(num):
	n1=0
	n2=1
	list=[]
	for i in range(1,num):
		list.append(n1)
		var=n1+n2
		n1=n2
		n2=var
	print list
