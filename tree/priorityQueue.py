"""
    优先队列
    还是用list实现, 借助于list的连续表技术
    Author: AkitaFriday
"""
# 自定义异常类


class PriQueueError(ValueError):
    def __init__(self, state):
        self.state = state

    def getMessage(self):
        print("********" + self.state + "********")


# 优先队列类实现


class PriorityQueue:
    def __init__(self, elist=[]):
        self._elems = list(elist)
        self._elems.sort(reverse=True)
    
    # 进队操作
    def enQueue(self, e):
        i = len(self._elems) - 1
        while i >= 0:
            if self._elems[i] <= e:
                i -= 1
            else:
                break
        self._elems.insert(i + 1, e)
    
    # 判断为空
    def is_empty(self):
        return not self._elems
    
    # 返回最后入队的元素
    def peek(self):
        try:
            if self.is_empty():
                raise PriQueueError("peek function error, because of null list")
            return self._elems[-1]
        except PriQueueError as pe:
            pe.getMessage()
    
    # 出队操作
    def deQueue(self):
        try:
            if self.is_empty():
                raise PriQueueError("deQueue function error, because of null list")
            return self._elems.pop()
        except PriQueueError as pe:
            pe.getMessage()


"""
    基于堆的优先队列
    Author: AkitaFriday
"""
class PriorityQueueByHeaps:
    def __init__(self, elist=[]):
        self._elems = list(elist)
        if elist:
            self.buildHeap()
    
    def is_empty(self):
        return not self._elems
    
    def peek(self):
        try:
            if self.is_empty():
                raise PriQueueError("peek function error, because of null list")
            return self._elems[0]
        except PriQueueError as pe:
            pe.getMessage()
    
    def enQueue(self, element):
        # 先创建一个空元素放在最后
        self._elems.append(None)
        self.siftUp(element, len(self._elems) - 1)
    
    # 向上过滤
    def siftUp(self, e, last):
        elems, i, j = self._elems, last, (last - 1) // 2
        while i > 0 and e < elems[j]:
            elems[i] = elems[j]
            i, j = j, (j - 1) // 2
        elems[i] = e
    
    # 出队
    def deQueue(self):
        try:
            if self.is_empty():
                raise PriQueueError("null list")
            elems = self._elems
            e0 = elems[0]
            e = elems.pop()
            if len(elems) > 0:
                self.siftDown(e, 0, len(elems))
            return e0
        except PriQueueError as pe:
            pe.getMessage()
    # 向下过滤
    def siftDown(self, e, begin, end):
        elems, i, j = self._elems, begin, begin * 2 + 1
        while j < end:
            if j + 1 < end and elems[j + 1] < elems[j]:
                j += 1
            if e < elems[j]:
                break
            elems[i] = elems[j]
            i, j = j, j * 2 + 1
        elems[i + 1] = e
    
    # 构建堆的过程
    def buildHeap(self):
        end = len(self._elems)
        for i in range(end // 2, -1, -1):
            self.siftDown(self._elems[i], i, end)