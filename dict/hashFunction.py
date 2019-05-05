"""
    除余法求散列值
    param:  key 关键码
    param:  length 散列表长度
    return: hashCode  散列值
"""
def hashCodeByMod(key, length):
    # 长度值乘10减去1就是散列表取值的最大值
    hash_length = length * 10 - 1
    if not isinstance(key, int):
        print("输入个整数吧")
    
    hashCode = (key % hash_length - 1)
    return hashCode


"""
    基数转换法求散列值
    param: key 关键码
    param: baseNum 基数
    param: length 散列表长度
"""
def hashCodeByBaseNum(key, baseNum, length):
    code_list = []
    list2 = []
    hashCode = 0
    # 如果输入的是字符串，就把字符转换成ascii码
    if not isinstance(key, int):
        for i in key:
            i = str(ord(i))
            code_list.append(i)
        key = int("".join(code_list))
    # 把数字按照十进制的位数拆开，把位数上的元素存在列表中，位数就是元素的下标
    while key // 10 > 0:
        list2.append(key % 10)
        key = key // 10
    list2.append(key % 10)
    # 基数转换, 把baseNum作为key的基数, 再将key转换成基数为10的数制
    for i in range(0, len(list2)):
        hashCode += list2[i] * baseNum ** i
    # 如果hashCode长度大于散列表的长度, 就对hashCode再进行一次取余
    if hashCode > length:
        hashCode = hashCodeByMod(hashCode, length)
    return hashCode

def main():
    key = "123FGH"
    print(hashCodeByBaseNum(key, 19, 1000))

# 测试
main()