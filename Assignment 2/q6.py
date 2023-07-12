def eight_queens(n=8):
	class DancingLink:
		class node:
			def __init__(self)->None:
				self.l=self.r=self
				self.u=self.d=self
				self.row=self.col=0
			def set(self,l,r,u=None,d=None,col=None)->None:
				self.l=l
				self.r=r
				self.u=u
				self.d=d
				self.col=col
		def __init__(self,n)->None:
			self.solution_set=[]
			self.cnt=[0 for i in range(0,n+1)]
			self.header=[self.node() for i in range(0,n+1)]
			self.leader={}
			for i in range(1,n):
				self.header[i].set(self.header[i-1],self.header[i+1],self.header[i],self.header[i],i)
			self.header[0].set(self.header[n],self.header[1],self.header[0],self.header[0],0)
			self.header[n].set(self.header[n-1],self.header[0],self.header[n],self.header[n],n)
		def link(self,x,y)->None:
			self.cnt[y]+=1
			p=self.node()
			if(self.leader.get(x)==None):
				self.leader[x]=p
				p.set(p,p)
			else:
				p.r=self.leader[x]
				p.l=self.leader[x].l
				self.leader[x].l.r=p
				self.leader[x].l=p
			p.u=self.header[y]
			p.d=self.header[y].d
			self.header[y].d.u=p
			self.header[y].d=p
			p.row=x
			p.col=y
		def cut(self,col)->None:
			self.header[col].l.r=self.header[col].r
			self.header[col].r.l=self.header[col].l
			i=self.header[col].d
			while i is not self.header[col]:
				j=i.r
				while j is not i:
					j.u.d=j.d
					j.d.u=j.u
					self.cnt[j.col]-=1
					j=j.r
				i=i.d
		def resume(self,col)->None:
			self.header[col].l.r=self.header[col]
			self.header[col].r.l=self.header[col]
			i=self.header[col].u
			while i is not self.header[col]:
				j=i.l
				while j is not i:
					j.u.d=j
					j.d.u=j
					self.cnt[j.col]+=1
					j=j.l
				i=i.u
		def dance(self,dep,lim)->bool:
			if dep>=lim:
				return True
			if self.header[0].r is self.header[0]:
				return False
			i=self.header[0].r
			val=lim*lim+1;pos=-1
			while i is not self.header[0]:
				if i.col>lim:
					break
				if self.cnt[i.col]<val:
					val=self.cnt[i.col]
					pos=i.col
				i=i.r
			self.cut(pos)
			i=self.header[pos].d
			while i is not self.header[pos]:
				self.solution_set.append(i.row)
				j=i.r
				while j is not i:
					self.cut(j.col)
					j=j.r
				if self.dance(dep+1,lim):
					return True
				j=i.l
				while j is not i:
					self.resume(j.col)
					j=j.l
				i=i.d
				self.solution_set.pop()
			self.resume(pos)
			return False

	Queens=DancingLink(6*n-2)
	for i in range(1,n+1):
		for j in range(1,n+1):
			Queens.link(n*(i-1)+j,n*0+j)
			Queens.link(n*(i-1)+j,n*1+i)
			Queens.link(n*(i-1)+j,n*2+i-j+n)
			Queens.link(n*(i-1)+j,n*4+i+j-2)
	if Queens.dance(0,n):
		ans=[[False]*n for i in range(n)]
		for val in Queens.solution_set:
			x,y=(val-1)//n,(val-1)%n
			ans[x][y]=True
		for i in range(n):
			for j in range(n):
				print("|",end=" Q"[ans[i][j]])
			print("|")
	else:
		print("No solution")

if __name__=='__main__':
	try:
		n=int(input("Input the number of the queens(1<=n<=100):\n(press enter to use default value n=8)\n"))
		assert 1<=n<=100
	except:
		n=8
	eight_queens(n)