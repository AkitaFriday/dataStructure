from lineTable import *


class circle_list(LinkedList):
	def __init__(self):
		self._rear = None

	# 判断是否空表，判断的条件从head是否为空变成判断rear尾节点是否为空
	def is_empty(self):
		return self._rear is None

	# 前端插入
	def prepend(self, elem):
		# 建立新的节点
		p = LNode(elem)
		if self._rear == None:
			# 建立一个节点的环
			p.next_ = p
			self._rear = p
		else:
			p.next_ = self._rear.next_
			self._rear.next_ = p
	# 尾端插入
	def append(self, elem):
		self.prepend(elem)
		self._rear = self._rear.next_

	# 首端弹出
	def pop(self):
		try:
			if self._rear is None:
				raise LinkedListError("Link List is null")
			p = self._rear.next_
			if self._rear is p:
				self._rear = None
			else:
				self._rear.next_ = p.next_
			return p.elem

		except LinkedListError as le:
			le.getMessage()

	# 遍历
	def readAll(self):
		if(self.is_empty()):
			return
		p = self._rear.next_
		while True:
			yield p.elem
			if p is self._rear:
				break
			p = p.next_