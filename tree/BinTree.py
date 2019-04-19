"""
    二叉树的实现
    Author: weiyc
"""
from stackAndQueue.queueByLineTable import Queue

# 二叉树节点类 , 整个结构是基于递归定义的
# 也就是说, left 或者 right 表示的可以是一个BinTreeNode对象
class BinTreeNode:
    def __init__(self, dat, left=None, right=None):
        self.data = dat
        self.left = left
        self.right = right


# 统计树中节点个数
def count_BinTreeNode(tree):
    if tree is None:
        return 0
    else:
        # 递归调用计算节点个数
        return 1 + count_BinTreeNode(tree.left) + count_BinTreeNode(tree.right)

# 求二叉树节点元素数值的和
def sum_BinTreeNode(tree):
    if tree is None:
        return 0
    else:
        return tree.data + sum_BinTreeNode(tree.left) + sum_BinTreeNode(tree.right)

"""
    二叉树的遍历
"""

# 先根序遍历, operation : 对具体节点的操作的方法名
def preRootOrder(tree, operation):
    if tree is None:
        return
    operation(tree.data)
    preRootOrder(tree.left, operation)
    preRootOrder(tree.right, operation)

# 宽度优先遍历


def printData(elem):
    print(elem, end="---->")

tree = BinTreeNode(1, BinTreeNode(2), BinTreeNode(3))
preRootOrder(tree, printData)

queue = Queue()
queue.is_empty()