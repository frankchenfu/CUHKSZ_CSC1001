# Algorithm 1: Using math conclusions
# from math import sqrt
# locker=[True if int(sqrt(i))**2==i else False for i in range(101)]
# print("The open lockers:",[i for i in range(1,101) if locker[i]])

# Algorithm 2: Bruteforce
def locker_puzzle():
	locker=[True for i in range(101)]
	for i in range(2,101):
		for j in range(i,101,i):
			locker[j]^=True
	return [i for i in range(1,101) if locker[i]]
if __name__=='__main__':
	print("The open lockers:",locker_puzzle())