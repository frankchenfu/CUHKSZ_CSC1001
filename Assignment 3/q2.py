class process_derivative:
	def __init__(self,ini:str="")->None:
		self.ini=ini
	def __str__(self)->str:
		if len(self.c)==0:
			return "0"
		res=""
		for i in self.c:
			if i[1]>=0:
				res+='+'
			if i[0]==0:
				res+=str(i[1])
				continue
			if i[1]==-1:
				res+='-'
			elif i[1]!=1:
				res+=str(i[1])+'*'
			res+=self.v
			if i[0]!=1:
				res+='^'+str(i[0])
		if res[0]=='+':
			res=res[1:]
		return res
	def print_derivative(self)->None:
		if len(self.d)==0:
			return "0"
		res=""
		for i in self.d:
			if i[1]>=0:
				res+='+'
			if i[0]==0:
				res+=str(i[1])
				continue
			if i[1]==-1:
				res+='-'
			elif i[1]!=1:
				res+=str(i[1])+'*'
			res+=self.v
			if i[0]!=1:
				res+='^'+str(i[0])
		if res[0]=='+':
			res=res[1:]
		return res
	def split_term(self,s:str)->list:
		if s[0] not in ['+','-']:
			s='+'+s
		res=[]
		pos=0
		while True:
			pa=s.find('+',pos+1)
			pb=s.find('-',pos+1)
			if pa==pb==-1:
				res.append(s[pos:].replace(' ',''))
				break
			elif pa==-1:
				res.append(s[pos:pb].replace(' ',''))
				pos=pb
			elif pb==-1:
				res.append(s[pos:pa].replace(' ',''))
				pos=pa
			else:
				res.append(s[pos:min(pa,pb)].replace(' ',''))
				pos=min(pa,pb)
		return res
	def analyze(self,s:str)->list:
		res=[]
		alphabets="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
		lx=list(set(alphabets)&set(s))
		assert(len(lx)<=1)
		if len(lx)==0:
			return "",[]
		x=lx[0]
		terms=self.split_term(s)
		for term in terms:
			num=term.split(sep=x)
			assert(len(num)<=2)
			if len(num)==1:
				if int(num[0]):
					res.append((0,int(num[0])))
				continue
			if len(num[0])==1:
				if num[0]=='+':
					cof=1
				else:
					cof=-1
			else:
				cof=int(num[0].rstrip('*'))
			if len(num[1])==0:
				deg=1
			else:
				deg=int(num[1].lstrip('^'))
			if cof:
				res.append((deg,cof))
		return x,res
	def differentiate(self)->list:
		return [(i[0]-1,i[0]*i[1]) for i in self.c if i[0]>0]
	def get_first_derivative(self)->None:
		try:
			self.v,self.c=self.analyze(self.ini)
			self.d=self.differentiate()
		except:
			return "invalid input!"
		else:
			return "The first derivative is: \'"+self.print_derivative()+'\''

if __name__=='__main__':
	s=input()
	p=process_derivative(s)
	print(p.get_first_derivative())