"""
    哈夫曼树
    哈夫曼树构造的思路:
        1. 先把指定集合的所有元素建立成单点二叉树，二叉树根节点的权值为元素值
        2. 把所有的单点二叉树放到优先队列中，排序规则按照根节点权值大小
        3. 从优先队列中出队两个权值最小的二叉树，构建一个新的二叉树，新二叉树根节点的权值为左右子树根节点权值的和
        4. 新二叉树入优先队列
        5. 重复 3，4步骤直到优先队列中只剩下一个元素
        6. 出队元素
"""
from BinTree import *
from priorityQueue import *

# 对二叉树节点类的扩充
class HuffmanTreeNode(BinTreeNode):
    # 节点比较大小，实际比较的是节点的data属性值的大小
    def __lt__(self, otherNode):
        return self.data < otherNode.data
    
    def __le__(self, otherNode):
        return self.data < otherNode.data


# 对优先队列的扩充
class HuffmanPriorityQueue(PriorityQueue):
    def number(self):
        return len(self._elems)


# 构造哈夫曼树的方法 参数为 实数集合
def createHuffmanTree(objSets):
    trees = HuffmanPriorityQueue()
    for i in objSets:
        trees.enQueue(HuffmanTreeNode(i))
    # 在队列元素不少于1时反复执行
    while trees.number() > 1:
        # 出队两个元素，因为优先队列的定义是从小到大排列，所以出队的两个一定是最小的两个
        child1 = trees.deQueue()
        child2 = trees.deQueue()
        # 两个元素的权值相加
        value = child1.data + child2.data
        # 新权值与左右子树构建新的二叉树，然后入队
        trees.enQueue(HuffmanTreeNode(value, child1, child2))
    return trees.deQueue()

