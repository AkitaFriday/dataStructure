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

# 测试方法
stack1 = Stack_lineTable()
stack1.push("1")
print(stack1.pop())