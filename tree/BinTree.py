"""
    二叉树的实现
    空树用None 表示
    非空二叉树 用列表[d, l, r]表示, d 代表根节点， l , r, 分别代表左子节点与右子节点
    Author: AkitaFriday
    P.S 这个实现玩砸了
"""
class BinTree:
    def __init__(self, data, left=None, right=None):
        self.tree = [data, left, right]

def readTree(Btree):
    i = 0
    while i < 3:
        if isinstance(Btree.tree[i], int):
            print(Btree.tree[i], end=" ")
        elif Btree.tree[i] is None:
            print("None", end=" ")   
        else:
            print("\n")
            readTree(Btree.tree[i]) 
        i += 1

btree = BinTree(1, BinTree(2), BinTree(3))

readTree(btree)