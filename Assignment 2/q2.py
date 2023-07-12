def emirps_100():
	p=set()
	pr=[True if i>=2 else False for i in range(10000)]
	for i in range(2,10000):
		if pr[i]:
			p.add(i)
			for j in range(i*2,10000,i):
				pr[j]=False
	ans=sorted([i for i in p if i!=int(str(i)[::-1]) in p])
	for i in range(100):
		print("%4d"%ans[i],end=" \n"[i%10==9])

if __name__=='__main__':
	emirps_100()