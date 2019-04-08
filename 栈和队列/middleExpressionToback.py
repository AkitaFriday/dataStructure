from stack import *

# 表达式优先级的字典, 为每个表达式规定一个优先级
priority = {
    "(": 1,
    "+": 3,
    "-": 3,
    "*": 5,
    "/": 5,
    "%": 5
}
# 表达式合集字符串
operation = "+-*/%()"

# 转换成后缀表达式


def trans_back_expression(line):
    operation_stack = Stack_lineTable()
    exp = []

    for x in tokens(line):
        # 数字直接进入后缀式列表
        if x not in operation:
            exp.append(x)
        # 左括号进运算符号栈
        elif operation_stack.is_empty() or x == "(":
            operation_stack.push(x)
        # 处理右括号的分支
        elif x == ")":
            while not operation_stack.is_empty() and operation_stack.top() != "(":
                exp.append(operation_stack.pop())
            # 找不到左括号，匹配失败
            if operation_stack.is_empty():
                raise SyntaxError("*********Missing '('*********")
            # 括号匹配成功，但是栈内没有运算操作符,弹出左括号，右括号也不进栈
            operation_stack.pop()
        # 接下来处理算术运算符
        else:
            # 如果栈顶的运算符优先级大,就出栈并加入到表达式列表, 反之就把新的运算符入栈
            while (not operation_stack.is_empty() and
                   priority[operation_stack.top()] >= priority[x]):
                exp.append(operation_stack.pop())
            operation_stack.push(x)
    """ 如果还有剩下的运算符在栈内，判断是否还有左括号，
        如果还有就是不匹配(左括号依赖右括号去匹配,
        循环一遍后还在栈里待着，铁定就是不匹配咯)"""
    while not operation_stack.is_empty():
        if operation_stack.top() == "(":
            raise SyntaxError("*********Missing '('*********")
        # 剩下的一股脑放到表达式列表
        exp.append(operation_stack.pop())
    
    return exp

def tokens(line):
    """
        生成器函数，生成line中的每一项,
        针对的是表达式字符串中可能存在零个或多个空格的情况
    """
    i, llen = 0, len(line)
    while i < llen:
        while line[i].isspace():
            i += 1
        if i >= llen:
            break
        if line[i] in operation:
            yield line[i]
            i += 1
            continue
        
        j = i + 1
        while j < llen and (not line[j].isspace() and line[j] not in operation):
            if(line[j] == "e" or line[j] == "E") and j + 1 < llen and line[j + 1] == "-":
                j += 1
            j += 1
        yield line[i : j]
        i = j

line = "(3 - 5) * (6 + 17 * 4) / 3"
x = trans_back_expression(line)
print(" ".join(x))