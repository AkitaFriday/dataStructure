from random import randint

from stackAndQueue.queueByLineTable import *
from tree.priorityQueue import *
"""
    离散事件系统模拟
    离散事件的特征:
        1. 系统运行中不断发生事件(事件存在随机性)
        2. 事件在某一时刻发生，可能会导致某事件在未来的发生
"""
# 通用的模拟器类
class Simulation:
    def __init__(self, duration):
        # 实例化一个事件队列
        self._eventQueue = Queue()
        self._time = 0
        # 事件允许执行的时间片
        self._duration = duration

    # 事件执行方法
    def run(self):
        while not self._eventQueue.is_empty():
            # 事件从优先队列取出
            event = self._eventQueue.dequeue()
            # 事件时间就是当前时间
            self._time = event.time()
            if self._time > self._duration:
                break
            # 模拟这个事件其运行可能产生新事件
            event.run()
    
    def add_event(self, event):
        self._eventQueue.enqueue(event)
    
    def cur_time(self):
        return self._time


"""
    公共事件类
"""
class Event:
    def __init__(self, event_time, host):
        self._ctime = event_time
        self._host = host
    
    def __lt__(self, other_event):
        self._ctime < other_event._ctime
    
    def __le__(self, other_event):
        self._ctime <= other_event._ctime
    
    def host(self):
        return self._host
    
    def time(self):
        return self._ctime
    
    def run(self):
        pass


# 海关检查模拟类
class Customs:
    def __init__(self, gate_num, duration, arrive_interval, check_interval):
        # 实例化模拟器
        self.simulation = Simulation(duration)
        # 等待的队列
        self.waitLine = Queue()
        # 处理时间
        self.duration = duration
        self.gates = [0] * gate_num
        self.total_wait_time = 0
        self.total_used_time = 0
        self.car_num = 0
        self.arrive_interval = arrive_interval
        self.check_interval = check_interval
    
    def wait_time_acc(self, n):
        self.total_wait_time += n
    
    def used_time_acc(self, n):
        self.total_used_time += n
    
    def car_count(self):
        self.car_num += 1
    
    def add_event(self, event):
        self.simulation.add_event(event)
    
    def cur_time(self):
        return self.simulation.cur_time()
    
    def enqueue(self, car):
        self.waitLine.enqueue(car)
    
    def has_queued_car(self):
        return not self.waitLine.is_empty()
    
    def next_car(self):
        return self.waitLine.dequeue()
    
    def find_gate(self):
        for i in range(len(self.gates)):
            if self.gates[i] == 0:
                self.gates[i] = 1
                return i
        return None
    
    def free_gate(self, i):
        if self.gates[i] == 1:
            self.gates[i] = 0
        else:
            raise ValueError("Clear gate error")
    
    # 实施模拟
    def simulate(self):
        Arrive(0, self)
        self.simulation.run()
        self.statistics()
    # 输出统计数据
    def statistics(self):
        print("模拟" + str(self.duration) + "分钟, 位置: " + str(len(self.gates)) + "窗口")
        print("共" + self.car_num + "通过")
        print("平均等待时间" + self.total_wait_time / self.car_num)
        print("平均通过时间" + self.total_used_time / self.car_num)
        i = 0
        while not self.waitLine.is_empty():
            self.waitLine.dequeue()
            i += 1
        print("共" + i + "辆车辆等待通过")

class Car:
    def __init__(self, arrive_time):
        self.time = arrive_time
    
    def arrive_time(self):
        return self.time
    
def event_log(time, name):
    print("事件: " + name + ", 发生于: " + str(time))


class Arrive (Event):
    def __init__(self, arrive_time, customs):
        Event.__init__(self, arrive_time, customs)
        customs.add_event(self)
    
    def run(self):
        time, customs = self.time(), self.host()
        event_log(time, "汽车到达")

        Arrive(time + randint(*customs.arrive_interval), customs)
        car = Car(time)
        if customs.has_queued_car():
            customs.enqueue(car)
            return
        i = customs.find_gate()
        if i is not None:
            event_log(time, "汽车检查")
            Leave(time + randint(*customs.check_interval), i, car, customs)
        else:
            customs.enqueue(car)

class Leave(Event):
    def __init__(self, leave_time, gate_num, car, customs):
        Event.__init__(self, leave_time, customs)
        self.car = car
        self.gate_num = gate_num
        customs.add_event(self)
    
    def run(self):
        time, customs = self.time(), self.host()
        event_log(time, "汽车离开")
        customs.free_gate(self.gate_num)
        customs.car_count()
        customs.used_time_acc(time - self.car.arrive_time())
        if customs.has_queued_car():
            car = customs.next_car()
            i = customs.find_gate()
            event_log(time, "汽车检查")
            customs.wait_time_acc(time - car.arrive_time())
            Leave(time + randint(*customs.check_interval), self.gate_num, car, customs)

car_arrive_interval = (1, 2)
car_check_time = (3, 5)
cus = Customs(3, 480, car_arrive_interval, car_check_time)
cus.simulate()
