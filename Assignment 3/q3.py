from random import random,sample,choice
class ecosystem:
	class Bear:
		def __init__(self,ver=-1)->None:
			self.ver=ver
	class Fish:
		def __init__(self,ver=-1)->None:
			self.ver=ver
	def print_river(self)->None:
		print([self.name[type(i)] for i in self.river])
	def __init__(self,r=1,b=0,f=0,n=1)->None:
		if not(type(r)==type(b)==type(f)==type(n)==int) or b+f>r or r<0 or b<0 or f<0:
			print("invalid input!")
			self.n=-1
			return
		self.name={self.Bear:"B",self.Fish:"F",type(None):"N"}
		self.river=[self.Bear() for i in range(b)]+\
			[self.Fish() for i in range(f)]+[None]*(r-b-f)
		self.river=sample(self.river,k=len(self.river))
		self.empty=set([i for i in range(0,r) if self.river[i]==None])
		self.n=n
	def next_pos(self,i)->int:
		tmp=random()
		if i==0:
			return [0,1][tmp<1/2]
		elif i==len(self.river)-1:
			return [-1,0][tmp<1/2]
		else:
			if tmp<1/3:
				return -1
			elif tmp<2/3:
				return 0
			else:
				return 1
	def move(self,dep)->None:
		for i in range(len(self.river)):
			if self.river[i]==None or self.river[i].ver>=dep:
				continue
			dir=i+self.next_pos(i)
			print("Animal: %s, Action: %d"%(self.name[type(self.river[i])],dir-i))
			if i==dir:
				self.river[i].ver=dep
				print("The current ecosystem after the action:")
				self.print_river()
				continue
			if self.river[dir]==None:
				self.river[i],self.river[dir]=self.river[dir],self.river[i]
				self.river[dir].ver=dep
				self.empty.discard(dir)
				self.empty.add(i)
			elif type(self.river[dir])==type(self.river[i]):
				self.river[i].ver=dep
				if len(self.empty)==0:
					print("The current ecosystem after the action:")
					self.print_river()
					continue
				pos=choice(list(self.empty))
				self.empty.discard(pos)
				if type(self.river[dir])==self.Bear:
					self.river[pos]=self.Bear(dep)
				else:
					self.river[pos]=self.Fish(dep)
			else:
				self.empty.add(i)
				if type(self.river[dir])==self.Fish:
					self.river[dir]=self.Bear(dep)
				self.river[i]=None
			print("The current ecosystem after the action:")
			self.print_river()
	def simulation(self)->None:
		if self.n==-1:
			return
		for i in range(self.n):
			print("The ecosystem at the beginnning of the step %d:"%(i+1))
			self.print_river()
			self.move(i)

if __name__=='__main__':
	e=ecosystem(5,2,1,3)
	e.simulation()