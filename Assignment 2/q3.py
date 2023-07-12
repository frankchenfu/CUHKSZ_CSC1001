def isValid(number:int)->bool:
	if not (13<=len(str(number))<=16):
		return False
	return not (sumOfDoubleEvenPlace(number)+sumOfOddPlace(number))%10
def sumOfDoubleEvenPlace(number:int)->int:
	return sum([getDigit(int(i)*2) for i in str(number)[-2::-2]])
def getDigit(number:int)->int:
	return number%10+number//10
def sumOfOddPlace(number:int)->int:
	return sum(map(int,str(number)[::-2]))

if __name__=='__main__':
	try:
		s=input("Enter your card number:")
		print("The card number is",["in",""][isValid(int(s))]+"valid.")
	except:
		print("The card number is invalid.")