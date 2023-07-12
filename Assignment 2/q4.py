def isAnagram(s1,s2)->bool:
	return sorted(list(s1))==sorted(list(s2))
if __name__=='__main__':
	s1,s2=input("Enter two words(separate by spaces)").split()
	print(["is not","is"][isAnagram(s1,s2)],"an anagram")