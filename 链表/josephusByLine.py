"""
	用线性表实现一下约瑟夫环问题，
	约瑟夫环问题: n个小朋友围成了一圈，从第k个人报数，类似于击鼓传花，
	到第m个人，就把他拉出来挠脚心，然后从下个人继续报数，按照一样的规则退出，
	直到所有人都被拉走，这时候列出各个出列的小朋友的编号
	解决思路:
		1. 建立一个n个元素的表
		2. 找到第k个人开始
		3. 向后数m个，然后把当前下标元素置0，遇到表的结尾，则从下标0开始循环
		4. n个元素都出列，结束循环
"""
from circleLinkList import *
# 基于数组概念的解
def josephus_array(n , k, m):
	# n： 总人数 k: 开始的人 m : 弹出操作的循环数
	people = list(range(1, 1 + n)) 

	i = k - 1
	# 外部循环次数为总人数
	for num in range(n):
		count = 0;
		# 当元素被置0时，count数不变，会继续循环，
		# 整个过程模拟有内容的元素循环报数
		while count < m:
			if people[i] > 0:
				count += 1
			if count == m:
				# 如果 count 等于 m 代表到达报数为m的位置，需要弹出,元素置0
				print(people[i], end="")
				people[i] == 0
			# 一次报数结束后，从该位置的下一位开始循环报数
			i = (i + 1) % n
		# 在最后一个数弹出前，不换行，但是给每个数后加上逗号
		if num < n - 1:
			print(", ", end="")
		else:
			print("")
	return

# 基于顺序表的解
def josephus_list(n, k, m):
	people = list(range(1, n + 1))

	num, i = n, k - 1
	# 采用表的处理方法，对于符合条件的元素，直接使用pop弹出该元素，表的长度越来越短，直到长度为零结束
	for num in range(n, 0, -1):
		i = (i + m - 1) % num
		print(people.pop(i), end=(", " if num > 1 else "\n"))
	return

# 基于链表的解
class josephus(circle_list):
	def turn(self, m):
		for i in range(m):
			self._rear = self._rear.next_

	def __init__(self, n, k, m):
		circle_list.__init__(self)
		for i in range(n):
			self.append(i + 1)
		self.turn(k - 1)
		while not self.is_empty():
			self.turn(m - 1)
			print(self.pop(), end="\n" if self.is_empty() else  ", ")
	

# 测试
josephus_array(10, 2, 7)

josephus_list(10, 2, 7)

josephus(10, 2, 7)