from stack import *

# 表达式优先级的字典, 为每个表达式规定一个优先级
priority = {
    ")": 1,
    "+": 3,
    "-": 3,
    "*": 5,
    "/": 5,
    "%": 5
}
# 表达式合集字符串
operation = "+-*/%()"


def tokens(line):
    """
        生成器函数，生成line中的每一项,
        这把是从后向前遍历, 因为是要做波兰表达式
        针对的是表达式字符串中可能存在零个或多个空格的情况
    """
    lists = []
    i, llen = 0, len(line)
    while i < llen:
        while line[i].isspace():
            i += 1
        if i >= llen:
            break
        if line[i] in operation:
            lists.append(line[i])
            i += 1
            continue

        j = i + 1
        while j < llen and (not line[j].isspace() and line[j] not in operation):
            if(line[j] == "e" or line[j] == "E") and j + 1 < llen and line[j + 1] == "-":
                j += 1
            j += 1
        lists.append(line[i: j])
        i = j
    # 偷懒， 从前往后遍历，然后来个reversed(), 还是个迭代器, 美滋滋
    return reversed(lists)


# 转波兰表达式
# 要点在于中缀式字符串的从后往前遍历s
def transToPolish(line):
    operation_stack = Stack_lineTable()
    exp = []

    for x in tokens(line):
        # 数字直接进入前缀式列表
        if x not in operation:
            exp.append(x)
        # 右括号进运算符号栈
        elif operation_stack.is_empty() or x == ")":
            operation_stack.push(x)
        # 处理左括号的分支
        elif x == "(":
            while not operation_stack.is_empty() and operation_stack.top() != ")":
                exp.append(operation_stack.pop())
            # 找不到右括号，匹配失败
            if operation_stack.is_empty():
                raise SyntaxError("*********Missing '('*********")
            # 括号匹配成功，但是栈内没有运算操作符,弹出右括号
            operation_stack.pop()
        # 接下来处理算术运算符
        else:
            # 如果栈顶的运算符优先级大,就出栈并加入到表达式列表, 反之就把新的运算符入栈
            # 此处 栈顶运算符必须大于新运算符，平级不行
            while not operation_stack.is_empty() and priority[operation_stack.top()] > priority[x]:
                exp.append(operation_stack.pop())
            operation_stack.push(x)
    """ 如果还有剩下的运算符在栈内，判断是否还有右括号，
        如果还有就是不匹配(左括号依赖右括号去匹配,
        循环一遍后还在栈里待着，铁定就是不匹配咯)"""
    while not operation_stack.is_empty():
        if operation_stack.top() == ")":
            raise SyntaxError("*********Missing '('*********")
        # 剩下的一股脑放到表达式列表
        exp.append(operation_stack.pop())

    return exp

# 波兰表达式计算


def calculatorPolish(line):
    operation_stack = Stack_lineTable()
    data_stack = Stack_lineTable()
    # 前缀式数组倒序遍历
    for i in line:
        # 操作符号栈为空并且当前是数字时, 数据栈入栈
        if i not in operation and operation_stack.is_empty():
            data_stack.push(int(i))
            continue
        else:
            operation_stack.push(i)
        # 一旦操作符号栈有元素, 就出栈进行计算
        x = operation_stack.pop()
        elem1 = data_stack.pop()
        elem2 = data_stack.pop()
        switch = {
            "+": elem1 + elem2,
            "-": elem1 - elem2,
            "*": elem1 * elem2,
            "%": elem1 % elem2,
            "/": elem1 / elem2
        }
        result = switch[x]
        # 计算的结果再次压栈进数据栈
        data_stack.push(result)
    print(data_stack.pop())



line = "1+2-3*(4-5)"
x = transToPolish(line)
result = []
for i in reversed(x):
    result.append(i)
print(" ".join(result))
calculatorPolish(x)
