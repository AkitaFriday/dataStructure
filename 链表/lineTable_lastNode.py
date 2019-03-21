from lineTable import *
from random import *

class lineTable_lastNode(LinkedList):
	def __init__(self):
		super().__init__()
		self._rear = None

	def prepend(self, elem):
		if self._head is None:
			self._head = LNode(elem, self._head)
			self._rear = self._head
		else:
			self._head = LNode(elem, self._head)
	def append(self, elem):
		if self._head is None:
			self._head = LNode(elem, self._head)
			self._rear = self._head
		else:
			self._rear.next_ = LNode(elem)
			self._rear = self._rear.next_

	def pop_last(self, elem):
		try:
			if self._head is None:
				raise LinkedListError("Link list is null")
			p = self._head
			if p.next_ is None:
				e = p.elem
				self._head = None
				return e
			while p.next_.next_ is not None:
				p = p.next_
			e = p.next_.elem
			p.next_ = None
			self._rear = p
			return e

		except LinkedListError as le:
			le.getMessage()


def mainFunction():
	link1 = lineTable_lastNode()
	for x in range(0, 10):
		link1.append(randint(1,100))
	value = link1.filter(lambda x: x % 2 == 0)
	for i in value:
		print(i)
mainFunction()