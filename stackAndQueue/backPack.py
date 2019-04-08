"""
    递归: 递归与函数的调用实际上就是在程序运行栈中暂存每次调用的局部信息
    用递归的方法解决背包问题, 背包问题描述: 一个背包中可以放总重量为weight的东西, 
    现在有 n个物体的集合S, 重量分别为weight0 ~ weightN, 问题，能否从中找出若干个物品，
    使得其总重量刚好等于weight
"""
def backPack_weight(weight, wlist, n):
    if weight == 0:
        return True
    if weight < 0 or (weight > 0 and n < 1):
        return False
    if backPack_weight(weight - wlist[n - 1], wlist, n - 1):
        return True
    if backPack_weight(weight, wlist, n - 1):
        return True
    else:
        return False


n = 10
wlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
weight = 55
result = backPack_weight(weight, wlist, 10)
print(result)