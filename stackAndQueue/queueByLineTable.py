"""
    实际上是用list实现一个队列
"""

# 这是一个异常类, 用于入队时关注队满，出队时关注队空
class QueueUnderFlowError(ValueError):
    def __init__(self, reason):
        self.reason = reason
    
    def getMessage(self):
        print("*********" + self.reason + "**********")


# 队列的类