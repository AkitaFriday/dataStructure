class QueueUnderFlowError(ValueError):
    def __init__(self, reason):
        self.reason = reason
    
    def getMessage(self):
        print("*********" + self.reason + "**********")


# 队列的类 : 非循环队列
class Queue():
    def __init__(self, init_len = 8):
        self._len = init_len
        # 初始化一个有确定长度的列表
        self._elems = [0] * init_len
        # 表头元素下标
        self._head = 0
        # 表中元素个数
        self._num = 0
    
    def is_empty(self):
        return self._num == 0

    def peek(self):
        try:
            if self._num != 0:
                return self._elems[self._head]
            else:
                raise QueueUnderFlowError("队空")
        except QueueUnderFlowError as qe:
            qe.getMessage()
    
    def dequeue(self):
        try:
            if self._num == 0:
                raise QueueUnderFlowError("队空")
            e = self._elems[self._head]
            # 出队操作, 头元素下标后移
            self._head = (self._head + 1) % self._len
            self._num -= 1
            return e
        except QueueUnderFlowError as qe:
            qe.getMessage()
    
    def enqueue(self, e):
        try:
            if self._len == self._num:
                self._extend()
            # 队尾的空位位置, 是头元素下标与元素总数之和 对列表长度取余的结果
            self._elems[(self._head + self._num) % self._len] = e
            self._num += 1
        except QueueUnderFlowError as qe:
            qe.getMessage()
    
    def _extend(self):
        
        old_len = self._len
        # 每次增长原有容量的两倍
        self._len *= 2
        new_elems = [0] * self._len
        # 把旧队列中的所有元素转移到新队列中
        for i in range(old_len):
            new_elems[i] = self._elems[(self._head + i) % old_len]
        self._elems, self._head = new_elems, 0


"""
    二叉树的实现
    Author: weiyc
"""

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
def levelOrder(tree, operation):
    operation(tree.data)
    levelOrderQueue = Queue()
    levelOrderQueue.enqueue(tree)
    while not levelOrderQueue.is_empty():
        node = levelOrderQueue.dequeue()
        # 如果弹出的树节点为空, 直接跳过
        if node is None:
            continue
        levelOrderQueue.enqueue(tree.left)
        levelOrderQueue.enqueue(tree.right)

# 非递归的先根序遍历 ,利用栈实现
def preRootOrderByStack(tree, operation):
    s = Stack()
    while tree is not None or not s.is_empty():
        while tree is not None:
            operation(tree.data)
            # 右子树入栈
            s.push(tree.right)
            # 从左子树不断深入
            tree = tree.left
        # 遇到叶子节点后回溯，从最近的右子树开始
        tree = s.pop()

# 递归的后序遍历，利用栈实现
def backRootOrderByStack(tree, operation):
    s = Stack()
    while tree is not None or not s.is_empty():
        while tree is not None:
            s.push(tree)
            tree = tree.left if  tree.left is not None else tree.right
        tree = s.pop()
        operation(tree.data)
        if not s.is_empty() and s.top().left == tree:
            t = s.top().right
        else:
            t = None

def printData(elem):
    print(elem, end="---->")

