"""
You are permitted to write code between Start and End.
Besides, you can write other extra functions or classes outside,
but don't change the template.
"""


class Node:
	def __init__(self, element, pointer):
		self.element = element
		self.pointer = pointer


class SinglyLinkedList:
	def __init__(self):
		self.head = None
		self.tail = None
		self.size = 0

	def insert(self, data):
		# Start writing your code.
		self.head = Node(data, self.head)
		self.size += 1
		# End writing your code.


def quick_sort(node):
	# Start writing your code.
	if node == None:
		return None
	siz = 0
	head = node
	while node != None:
		siz += 1
		node = node.pointer
	from random import randint
	pos = randint(0, siz-1)
	node = head
	while pos > 0:
		pos -= 1
		node = node.pointer
	avr = node.element
	ls = rs = mid = None
	node = head
	while node != None:
		nxt = node.pointer
		if node.element < avr:
			node.pointer = ls
			ls = node
		elif node.element > avr:
			node.pointer = rs
			rs = node
		else:
			node.pointer = mid
			mid = node
		node = nxt
	ls = quick_sort(ls)
	rs = quick_sort(rs)
	ptr = None
	head = None
	node = ls
	while node != None:
		ptr = node
		node = node.pointer
	if ptr != None:
		head = ls
		ptr.pointer = mid
	else:
		head = mid
	node = mid
	while node != None:
		ptr = node
		node = node.pointer
	ptr.pointer = rs
	return head
	# End writing your code.


# We will utilize the code similar to the following to check your answer.
if __name__ == '__main__':
	test_list = SinglyLinkedList()
	nums = [4,2,3,1,0,5]  # An example.
	for num in nums:
		test_list.insert(num)
	first_node = test_list.head  # Get the first node of the linked list.
	print('The number of nodes in test_list is:')
	p = quick_sort(first_node)
	while p.pointer != None:
		print(p.element)
		p = p.pointer
	print(p.element)
