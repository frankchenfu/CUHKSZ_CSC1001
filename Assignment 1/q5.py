try:
	n=int(input("N = "))
	assert n>=1
except:
	print("Invalid input")
	exit(0)
pr=[True for i in range(0,n+1)]
print("The prime numbers smaller than %d include:"%n)
tot=0
for i in range(2,n+1):
	if pr[i]:
		print(i,end=" \n"[tot==7])
		tot=(tot+1)%8
		for j in range(i*2,n+1,i):
			pr[j]=False