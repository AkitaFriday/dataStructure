"""
    prim算法
    基本做法:
            从一个顶点出发，不断扩充包含该节点的部分生成树T
        步骤:
            1. 从图G(v, e)中取出一个顶点，组成一棵单点树T(u, er), 并把顶点加入集合u <u 是v的真子集>
            2. 检查所有G(v, e)中顶点vi在u中 , vj 在 v-u集合中的边， 并从中取最小的边，加入边集er, 顶点v加入顶点集v
            3. 重复以上步骤，直到集合中有n-1条边
"""
from tree.priorityQueue import *
from graph import *

def prim(graph):
    vnum = graph.vertex_num()
    mst = [None] * vnum
    cands = PriorityQueue([0, 0, 0])                 # 记录候选边(w, vi, vj)
    count = 0
    while count < vnum and not cands.is_empty():
        w, u, v = cands.deQueue()                    # 取出最短的边             
        if mst[v]:
            continue                                 # 邻接顶点v在mst的继续
        mst[v] = ((u, v), w)                         # 记录新的mst边和顶点
        count += 1
        for vi, w in graph.out_edges(v):             # 考虑v的邻接顶点vi
            if not mst[vi]:                          # 如果vi不在mst则这条边是候选边
                cands.enQueue((w, v, vi))
    return mst