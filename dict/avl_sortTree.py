"""
    平衡二叉排序树
    平衡二叉树: 或为空树，或者当前节点的左右子树高度之差为 1 或 0 或 -1
    author: weiyc
"""
from tree.BinTree import *
from dict.binSortTree import *

# 新定义二叉树节点，初始化增加平衡因子参数
class AVLBinTreeNode(BinTreeNode):
    def __init__(self, data):
        super.__init__(self, data)
        # 平衡因子初始为0
        self.bf = 0

# 树类: 继承之前的二叉排序树
class AVLDict(DictBinTree):
    def __init__(self):
        super.__init__(self)

# 进行LL调整的静态方法, 增加的新节点在b的左子树的左子树
@staticmethod
def LL(a, b):
    # 把b的右子树赋给a的左子树
    a.left = b.right
    # 把a赋给b的右子树
    b.right = a
    # 调整完后把平衡因子归零
    a.bf = b.bf = 0
    return b

# RR调整的操作与LL相似，把子树赋值操作对象对调
@staticmethod
def RR(a, b):
    a.right = b.left
    b.right = a
    a.bf = b.bf = 0
    return b

# LR型调整 
# 参数a : df值 >1 或 <-1的节点
# 参数b ：插入新元素的子树  
@staticmethod
def LR(a, b):
    c = b.right
    b.right, a.left = c.left, c.right
    c.left, c.right = b, a
    # c节点后左右子树都有插入
    if c.bf == 0:
        a.bf = b.bf = 0
    # c节点插入左子树的情况,a节点没有左子 
    elif c.bf == 1:
        a.bf = -1
        b.bf = 0
    # c节点插入右子树的情况，b节点没有右子
    else:
        a.bf = 0
        b.bf = 1
    # 返回调整后的子树根节点
    return c

# RL型调整
# 参数a : df值 >1 或 <-1的节点
# 参数b ：插入新元素的子树
@staticmethod
def RL(a, b):
    c = b.left
    b.left, a.right = c.right, c.left
    c.left, c.right = a, b
    if c.bf == 0:
        a.bf = b.bf = 0
    elif c.bf == 1:
        a.bf = 0
        b.bf = -1
    else:
        a.bf = 1
        b.bf = 0