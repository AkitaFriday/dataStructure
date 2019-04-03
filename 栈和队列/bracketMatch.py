"""
括号匹配, 栈的经典应用场景
思路:
    1. 循环遍历文本, 遇到开括号就入栈
    2. 遇到闭括号, 弹出栈顶元素并进行匹配
    3. 匹配, 就继续操作, 不匹配, 操作结束, 返回失败信息
"""
from  stack import *

def bracket_match(text):
    # text是被检查的文本
    parens = "()[]{}"
    open_parens = "([{"
    # 表示匹配关系的字典
    matchDict = {
        "}" : "{",
        "]" : "[",
        ")" : "("
    }

    # 内部函数, 括号生成器, 每次返回text 里下一个符号和对应的下标
    def bracket_gen(text):
        i, text_len = 0, len(text)
        while True:
            while i < text_len and text[i] not in parens:
                i += 1
            if i >= text_len:
                return
            yield text[i], i
            i += 1
    
    obj = Stack_lineTable()

    for pr , i in bracket_gen(text):
        if pr in open_parens:
            obj.push(pr)
            print(pr)
        elif obj.pop() != matchDict[pr]:
            print("匹配" + pr + "出现失败. 位置是: " , i)
            return False
    print("匹配成功")
    return True


text = "{{})}"
print(bracket_match(text))