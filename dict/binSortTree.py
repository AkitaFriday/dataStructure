"""
    二叉排序树
"""
from tree.BinTree import *

"""
    假设这是一个字典结构,有关键码key 和值value
"""
class Assoc:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class DictBinTree:
    def __init__(self):
        self._root = None
    
    def is_empty(self):
        return self._root is None
    
    def serach(self, key):
        bt = self._root
        if bt is not None:
            entry = bt.data
            # 关键码小于节点的关键码，继续向左递归
            if key < entry.key:
                bt = bt.left
            # 关键码大于节点关键码，继续向右递归
            elif key > entry.data:
                bt = bt.right
            # 找到位置，返回值
            else:
                return entry.value
        return None
    
    def insert(self, key, value):
        bt = self._root
        # 如果根节点为空，在根节点创建节点
        if bt is None:
            self._root = BinTreeNode(Assoc(key, value))
            return
        while True:
            entry = bt.data
            # 如果关键码小于节点关键码，但是左子节点为空，就在左子节点创建新的节点插入关键码与对应的值，反之继续向左子递归
            if key < entry.key:
                if bt.left is None:
                    bt.left = BinTreeNode(Assoc(key, value))
                    return
                bt = bt.left
            # 如果关键码大于节点关键码，但是右子节点为空，就在右子节点创建新的节点插入关键码与对应的值，反之继续向右子递归
            elif key > entry.key:
                if bt.right is None:
                    bt.right = BinTreeNode(Assoc(key, value))
                    return
                bt = bt.right
            # 找到位置，改变关键码对应的值并退出循环
            else:
                bt.data.value = value
                return
        
    def delete(self, key):
        p, q = None, self._root
        while q is not None and q.data.key != key:
            p = q
            if key < q.data.key:
                q = q.left
            else:
                q = q.right
            if q is None:
                return
            # 如果q的左节点为空
            if q.left is None:
                # 如果q是根节点, 把q的右子当做根节点
                if p is None:
                    self._root = q.right
                # 如果q是p的左子, 把q的右子赋给p的左子
                elif q is p.left:
                    p.left = q.right
                # 如果q是p的右子，把q的右子赋给p的右子
                else:
                    p.right = q.right
                return
            # r是q的左子
            r = q.left
            # 如果r的右子不为空, 递归找到r的最右子节点，并且把q的右子节点放在r的最右叶子节点之后，作为新的最右叶子节点
            while r.right is not None:
                r = r.right
            r.right = q.right
            # 如果q是根节点, 把q的左子赋给根节点
            if p is None:
                self._root = q.left
            # 如果q是p的左子节点，把q的左子赋值给p的左子
            elif p.left is q:
                p.left = q.left
            # 如果q是p的右子，把q的左子赋值给p的右子
            else:
                p.right = q.left
