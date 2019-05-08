"""
    几个简单的排序算法
    author: weiyc 2019-05-08
"""
import random
import time
import matplotlib.pyplot as plt

# 数据元素类，假设将要排序的序列中的每个元素是以下定义的类的实例对象
class Item(object):
    def __init__(self, key, datum):
        self.key = key
        self.datum = datum

# 插入排序
# 就是调整第i个元素在下标[0, i]范围的顺序，i从下标1扩充到len(list) - 1时，就最终生成了整个list的排序序列

def insert_sort(lst):
    # 序列只有一个元素认为是有序的
    for i in range(1, len(lst)):
        x = lst[i]
        j = i
        # 每一次循环时，lst[i] 之前的元素都是有序的
        while j > 0 and lst[j - 1].key > x.key:
            lst[j] = lst[j - 1]
            j -= 1
        lst[j] = x
    return lst

# 生成随机列表
def rand_list(num):
    lst = []
    if num > 2000000000:
        return
    for i in range(num):
        lst.append(Item(random.randint(1, num * 7), random.randint(1, num * 7)))
    return lst

# 冒泡排序
def bubble_sort(lst):
    for i in range(len(lst)):
        found = False
        for j in range(1, len(lst) - i):
            if lst[j - 1].key > lst[j].key:
                lst[j - 1], lst[j] = lst[j], lst[j - 1]
                # 存在逆序，就将相邻的逆序元素位置互换，并把found置true
                found = True
        # 内层循环遍历一遍列表未发现逆序，说明列表是有序的，直接退出循环
        if not found:
            break
    return lst

# 交错冒泡, 正向扫描一遍后，再反向扫描寻找逆序对
# 第一层循环，从0开始,到最后一个元素
# 第二层循环，从1开始，到
def cross_bubble_sort(lst):
    for i in range(len(lst)):
        found = False
        if (i % 2 == 0):
            for j in range(1, len(lst) - i):
                if lst[j - 1].key > lst[j].key:
                    lst[j - 1], lst[j] = lst[j], lst[j - 1]
                    found = True
        else:
            for j in range(len(lst) - i - 1, 0, -1):
                if lst[j - 1].key > lst[j].key:
                    lst[j - 1], lst[j] = lst[j], lst[j - 1]
                    found = True
        if not found:
            break
    return lst

# 快速排序
def quick_sort(lst):
    # 快速排序递归划分实现
    def qsort_req(lst, l, r):
        if l >= r:
            return
        i = l
        j = r
        # 局部变量，保存调整记录位置
        pivot = lst[i]        # list[i] 是初始空位
        # 当i = j时一次扫描结束
        while i < j:
            while i < j and lst[j].key >= pivot.key:
                j -= 1                                  # 用j向左扫描寻找小于pivot的记录，
            if i < j:
                lst[i] = lst[j]
                i += 1                                  # 小记录移到左边
            while i < j and lst[i].key <= pivot.key:
                i += 1                                  # 用i向右扫描大于pivot的记录
            if i < j:
                lst[j] = lst[i]
                j -= 1                                  # 大记录移到右边
        lst[i] = pivot                                  # pivot 存入最终位置
        qsort_req(lst, l, i-1)                          # 左半区继续递归
        qsort_req(lst, i+1, r)                          # 右半区继续递归
    # 执行快速排序划分
    qsort_req(lst, 0, len(lst) - 1)
# 方法执行时间计算函数
def runTimeCal(function1):
    START = time.time()
    function1(rand_list(1000))
    END = time.time()
    return END - START

list1 = []
list2 = []
list3 = []
list4 = []
times = []

for i in range(30):
    list1.append(runTimeCal(bubble_sort))
    list2.append(runTimeCal(cross_bubble_sort))
    list3.append(runTimeCal(insert_sort))
    list4.append(runTimeCal(quick_sort))
    times.append(i)

# 画图比较几种排序的效率
# 从图结果可得到的是，插入排序把两种冒泡吊起来打了
fig = plt.figure(figsize=(10, 6))
plt.plot(times, list1, c="red", label="bubble_sort")
plt.plot(times, list2, c="blue", label="cross_bubble_sort")
plt.plot(times, list3, c="yellow", label="insert_sort")
plt.plot(times, list4, c="black", label="quick_sort")
plt.legend(loc="upper left")
plt.xlabel("test times")
plt.ylabel("per operation time")
plt.show()