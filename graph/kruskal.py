"""
    边表的形式(w(i, j), v(i), v(j))
    w代表权值，v(i), v(j)代表两端点
"""
from graph import *

def kruskal(graph):
    vnum = graph.vertex_num()
    reps = [i for i in range(vnum)]
    mst, edges = [], []
    # 把所有的边放到edges列表中
    for vi in range(vnum):
        for v, w in graph.out_edges(vi):
            edges.append((w, vi, v))
    # 边表从小到大排序
    edges.sort()
    for w, vi, vj in edges:
        if reps[vi] != reps[vj]:                 # 两端点不属于同一个连通分量
            mst.append(((vi, vj), w))            # 记录这条边
            if len(mst) == vnum - 1:             # 记录n - 1条边后，记录结束,退出构造
                break
            rep, orep = reps[vi], reps[vj]
            for i in range(vnum):                # 合并连通分量
                if reps[i] == orep:
                    reps[i] = rep
    return mst