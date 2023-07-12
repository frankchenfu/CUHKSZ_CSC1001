from math import pi,sin,cos,tan
try:
	func=input("Enter function name:")
	a,b,n=input("Enter a,b and n:").split()
	a=float(a);b=float(b);n=int(n)
	assert func in ["sin","cos","tan"]
	assert n>=1
	assert a<b
	if func=="tan":
		assert (a-pi/2)//pi==(b-pi/2)//pi
except:
	print("Invalid input")
	exit(0)
sum=.0
for i in range(1,n+1):
	sum+=eval(func+"(a+(b-a)/n*(i-0.5))")
sum*=(b-a)/n
print("The numerical integration is",sum)