try:
	n=int(input("N = "))
	assert n>=1
except:
	print("Invalid input")
	exit(0)
print("%-8s%-8s%-8s"%("m","m+1","m**(m+1)"))
for i in range(1,n+1):
	print("%-8d%-8d%-8d"%(i,i+1,i**(i+1)))