"""
You are permitted to write code between Start and End.
Besides, you can write other extra functions or classes outside,
but don't change the template.
"""


def HanoiTower(n, from_rod='A', aux_rod='B', to_rod='C'):
	result_list = []
	# Start writing your code.
	chr = [from_rod, aux_rod, to_rod]
	opt = [(0, 1, 2, n)]
	while len(opt) > 0:
		u, k, v, m = opt.pop()
		if m == 1:
			result_list.append("%s --> %s" % (chr[u], chr[v]))
			continue
		opt.append((k, u, v, m-1))
		opt.append((u, k, v, 1))
		opt.append((u, v, k, m-1))
	# End writing your code.
	return result_list


"""
You should store each line your output in result_list defined above.
For example, if the outputs of print() are: 
				A --> C
				A --> B
then please store them in result_list:

strs = "A --> C"
result_list.append(strs)
strs = "A --> B"
result_list.append(strs)

Thus, once you want to print something, please store them in result_list immediately, 
rather than utilizing print() to print it. 
Don't miss the space! For example, don't output:
				A-->C
				A-->B

We will utilize the code similar to the following to check your answer.
"""

if __name__ == '__main__':
	n = 3
	result_list = HanoiTower(n)
	for item in result_list:
		print(item)
