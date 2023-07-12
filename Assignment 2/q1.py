def sqrt(n:float):
	if n<0:
		return None
	eps=1e-5
	las=1.0
	while True:
		nxt=(las+(n/las))/2
		if abs(nxt-las)<eps:
			break
		las=nxt
	return las

if __name__=='__main__':
	try:
		n=float(input("Please input a positive real number:"))
		print("%.4f"%sqrt(n))
	except:
		print("Invalid input.")