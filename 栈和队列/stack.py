# 自定义异常类
class StackUnderFlowError(ValueError):
    def getMessage(self):
        print("栈空异常")


# 栈的顺序表实现类
class Stack_lineTable(list):
    # 初始化时初始化一个空list, 利用python内置的list实现栈
    def __init__(self):
        self.stack = list()
    # 判断栈空
    def is_empty(self):
        return self.stack == []
    # 入栈操作
    def push(self, elem):
        self.stack.append(elem)
    # 出栈操作
    def pop(self):
        try:
            if len(self.stack) <= 0:
                raise StackUnderFlowError
            else:
                return self.stack.pop()
        except StackUnderFlowError as se:
            se.getMessage()
    # 获取栈顶元素
    def top(self):
        try:
            if len(self.stack) <= 0:
                raise StackUnderFlowError
            else:
                return self.stack[-1]
        except StackUnderFlowError as se:
            se.getMessage()

"""
    用单向链表实现一个栈
"""
# 节点类
class Node(object):
    def __init__(self, elem, next_ = None):
        self.next_ = next_
        self.elem = elem
# 用链表实现栈的类
class Stack_linkedList:
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head is None
    def push(self, elem):
        self.head = Node(elem, self.head)
    
    def pop(self):
        try:
            if self.head is None:
                raise StackUnderFlowError
            p = self.head
            self.head = p.next_
            return p.elem
        except StackUnderFlowError as se:
            se.getMessage()
    
    def top(self):
        return self.head.elem
# 测试方法
stack2 = Stack_linkedList()
print(stack2.is_empty())
stack2.push("1")
stack2.push("2")
print(stack2.pop())
print(stack2.top())
