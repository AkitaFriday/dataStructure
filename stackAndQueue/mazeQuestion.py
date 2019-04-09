from stack import *
from copy import *
from queueByLineTable import *

"""
    迷宫问题求解，对于状态空间搜索和缓存结构的应用，
    准备使用栈和队列两种方法
    maze是一个二维数组,用来模拟一个矩阵 格式类似:[[0, 0], [0, 1], [1, 0], [1, 1]]
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)], 表示每次移动操作,分别表示 右移1, 下移1, 左移1, 上移1
"""

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# 把迷宫maze的pos位置的元素置为2


def mark(maze, pos):
    maze[pos[0]][pos[1]] = 2

# 检查迷宫maze的pos位置是否是可行的


def passable(maze, pos):
    return maze[pos[0]][pos[1]] == 0


"""
    递归求解迷宫
    思路: 从当前位置寻找迷宫出口，如果当前位置恰好是迷宫出口，那么问题结束
    逐个检查当前位置的四邻位置，是否可以到达出口,
    递归的方法是从出口倒推入口
"""


def find_path_recursion(maze, pos, end):
    mark(maze, pos)
    if pos == end:
        print(pos, end=" ")
        return True
    for i in range(4):
        # 考虑下一个可能的邻接方向
        nextPos = pos[0] + dirs[i][0], pos[1] + dirs[i][1]
        # 邻接位置可行, 递归调用结束，否则不断递归直到循环结束
        if passable(maze, nextPos):
            if find_path_recursion(maze, nextPos, end):
                print(pos, end=" ")
                return True
    return False


"""
    栈结构，回溯法实现迷宫问题
"""


def maze_path_solver(maze, start, end):
    if start == end:
        print(start)
        return
    stack_pos = Stack_lineTable()
    mark(maze, start)
    # 把当前位置与下一探查方向0组成的元组入栈
    stack_pos.push((start, 0))
    while not stack_pos.is_empty():
        pos, next = stack_pos.pop()
        # 检索剩下的未探查方向，是否满足条件
        for i in range(next, 4):
            # 算出下一个位置
            nextPos = pos[0] + dirs[i][0], pos[1] + dirs[i][1]
            # 找到了出口，开始输出路径
            if nextPos == end:
                print_path(end, pos, stack_pos)
                return
            if passable(maze, nextPos):
                # 当前位置与探查方向入栈
                stack_pos.push((pos, i + 1))
                # 给探查过的位置打标签
                mark(maze, nextPos)
                # 将下一位置与探查方向0入栈, 开始下一位置的探查
                stack_pos.push((nextPos, 0))
                break
    print("找不到路径")


def print_path(end, pos, stack):
    print(end, end=" ")
    print(pos, end=" ")
    while not stack.is_empty():
        print(stack.pop()[0], end=" ")
    print("\n")


"""
    用队列作为缓存结构的实现
"""


def maze_path_queue(maze, start, end):
    map = dict()
    if start == end:
        print(start)
    return
    queue_maze = Queue()
    mark(maze, start)
    queue_maze.enqueue(start)
    while not queue_maze.is_empty():
        pos = queue_maze.dequeue()
        for i in range(4):
            nextP = pos[0] + dirs[i][0], pos[1] + dirs[i][1]
            if passable(maze, nextP):
                if nextP == end:
                    print("找到路径")
                    return
                mark(maze, nextP)
                queue_maze.enqueue(nextP)
    print("妹找着")
# 主方法


def main():
    maze = [
        [1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 1],
        [0, 0, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1],
        [1, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 0, 1]
    ]
    """ 
        此处不能用 = 复制数据，因为这玩意是浅拷贝,深层次上是同一个对象
        ,要不然第二个函数用的就是被第一个函数改变后的maze了
    """
    maze1 = deepcopy(maze)
    pos = 2, 0
    end = 5, 4
    find_path_recursion(maze, pos, end)
    print("\n")
    maze_path_solver(maze1, pos, end)


main()
