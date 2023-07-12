class Flower:
	def __init__(self,name:str="rose",petal:int=30,price:float=10.0)->None:
		self.name=name
		self.petal=petal
		self.price=price
	def setname(self,name:str)->None:
		self.name=name
	def setpetal(self,petal:int)->None:
		self.petal=petal
	def setprice(self,price:float)->None:
		self.price=price
	def __str__(self):
		if type(self.name)!=str:
			return "The input of the flower name is incorrect. A string is required."
		if type(self.petal)!=int or self.petal<0:
			return "The input of the number of petals is incorrect. An integer is required."
		if type(self.price)!=float or self.price<0:
			return "The input of the price is incorrect. A type of float is required."
		return "Here is the information of your flower. "+\
		"Name: "+self.name+", Number of petals: "+str(self.petal)+", price: "+str(self.price)
	def Information(self):
		return self.__str__()

if __name__=="__main__":
	rose=Flower("rose",5,7.0)
	print(rose.Information())