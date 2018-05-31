a=int(raw_input())
fac=1
if(a==0):
    print('the factorial is 1')
elif(a<0):
    print('factorial doesnt exist')
else:
    for i in range(1,a+1):
	fac=fac*i
	print(fac)
