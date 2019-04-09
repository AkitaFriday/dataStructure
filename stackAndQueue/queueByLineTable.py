"""
    实际上是用list实现一个队列
"""

# 这是一个异常类, 用于入队时关注队满，出队时关注队空
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

