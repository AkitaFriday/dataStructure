"""
    后缀表达式的运算
    思路:
        1. 把运算表达式拆成每个字符为一项的列表
        2. 遍历字符列表, 如果是浮点数就入栈
        3. 如果是运算符, 就出栈两个元素, 根据运算符进行计算
        4. 运算结果入栈, 重复步骤2, 直到栈中的元素数量小于2
"""
from stack import *

class expressionException(Exception):
    def __init__(self, message):
        self.message = message
    
    def getMessage(self):
        print(self.message)

class expressionStack(Stack_lineTable):
    def getLength(self):
        return len(self.stack)

def charSplit(line):
    lists = line.split(" ")
    return lists

def expression_calculator(expression_list):
    # 实例化一个表达式计算栈
    expression_stack = expressionStack()
    # 表达式模式串
    operation = "+-*/%"
    # 遍历
    try:
        for x in expression_list:
            # 如果不是操作符，就执行入栈操作
            if x not in operation:
                expression_stack.push(float(x))
                continue
            # 如果栈内元素小于2时，引发异常
            if expression_stack.getLength() < 2:
                raise expressionException("栈元素不够, 请检查表达式")
            elem1 = expression_stack.pop()
            elem2 = expression_stack.pop()
            switch = {
                "+" : elem1 + elem2,
                "-" : elem1 - elem2,
                "*" : elem1 * elem2,
                "%" : elem1 % elem2,
                "/" : elem1 / elem2
            }
            try:
                expression_stack.push(switch[x])
            except KeyError:
                print("零除错误")
        if expression_stack.getLength() == 1:
            return expression_stack.pop()
    except expressionException as ex:
        ex.getMessage()
        
# 测试方法
line = "3 5 - 6 17 4 * + * 3 /"
line = charSplit(line)

print(expression_calculator(line))