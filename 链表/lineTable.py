# 这是一个简单的单链表的实现
# 包括节点的定义，链表的定义
# 以及链表的常见方法实现

# 异常处理类
class LinkedListError(ValueError):
	def __init__(self, error):
		self.error = error
	def getMessage(self):
		print("***********************" + self.error + "**************************")

# 链表节点类
class LNode(object):
	"""链表的节点类"""
	def __init__(self, elem, next_ = None):
		self.elem = elem
		self.next_ = next_

class LinkedList:
	# 初始化 链表的head节点为空
	def __init__(self):
		self._head = None
	# 判断是否为空链表
	def is_empty(self):
		return self._head is None
	# 表头插入节点
	def prepend(self, elem):
		# 创建新节点赋给新头节点，并把原头节点赋给新头结点的next
		self._head = LNode(elem, self._head)

	# 删除头结点并获得头结点的数据// 就是出栈操作，以后估计要用这个单链表模拟栈
	def pop(self):
		if (self._head is None):
			raise LinkedListError("pop")
		e = self._head.elem
		self._head = self._head.next_
		return e

	# 在链表结尾增加新数据
	def append(self, elem):
		if self._head is None:
			self._head = LNode(elem)
			return 
		p = self._head
		while p.next_ is not None:
			p = p.next_
		p.next_ = LNode(elem)

	# 弹出最后一个节点的数据并删除
	def pop_last(self):
		if self._head is None:
			raise LinkedListError("pop_last")
		p = self._head
		
		if p.next_ is None:
			e = p.elem
			self._head = None
			return e

		while p.next_.next_ is not None:
			p = p.next_
		e = p.next_.elem
		p.next_ = None
		return e

	# 查找
	def find(self, elem):
		index = 0;
		if self._head is None:
			raise LinkedListError("find")
		p = self._head
		while p.next_ is not None:
			if (p.elem == elem):
				return index
			p = p.next_
			index += 1
		if(p.elem == elem):
			return index
		else:
			return "not found"

	# 遍历
	def readAll(self):
		value = []
		try:
			if self._head is None:
				raise LinkedListError("LinkList is null")
			p = self._head
			while p is not None:
				value.append(p.elem)
				p = p.next_
			return value
		except LinkedListError as le:
			le.getMessage()
	# 链表元素遍历, 生成器
	def elements(self):
		try:
			if self._head is None:
				raise LinkedListError("LinkList is null")
			p = self._head
			while p is not None:
				yield p.elem
				p = p.next_
		except LinkedListError as le:
			le.getMessage()

	# 筛选方法, 筛选生成器
	# 变量可以是函数名也可以是一个lambda表达式
	def filter(self, function):
		try:
			if self._head is None:
				raise LinkedListError("LinkList is null")
			p = self._head
			while p is not None:
				if (function(p.elem)):
					yield p.elem
				p = p.next_
		except LinkedListError as le:
			le.getMessage()

# 用于筛选的方法
def oushu(data):
	if (data % 2 == 0):
		return True
	else:
		return False


