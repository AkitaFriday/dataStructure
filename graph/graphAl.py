from graph import *
from graph import GraphError
"""
    邻接表实现的图
"""
class GraphAL(Graph):
    def __init__(self, mat=[], unconn=0):
        vnum = len(mat)
        try:
            for x in mat:
                if not len(x) == vnum:
                    raise ValueError("传入参数错误，请检查参数")
            self._mat = [mat[i][:] for i in range(vnum)]
            self._unconn = unconn
            self._vnum = vnum
        except ValueError:
            print("参数错误")
    
    # 增加新节点的方法: 增加新节点就是在顶点顺序表中增加一个位置并给它初始化新的关联表
    def add_vertex(self):
        self._mat.append([])
        self._vnum += 1
        # 返回添加的新节点的下标
        return self._vnum - 1
    
    # 增加新边的操作
    def add_edge(self, vi, vj, val=1):
        if self._vnum == 0:
            raise GraphError("长度为0")
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError("参数不可用")
        
        row = self._mat[vi]
        i = 0
        while i < len(row):
            if row[i][0] == vj:
                self._mat[vi][i] = (vj, val)
                return
            if row[i][0] > vj:
               break
            i += 1
        self._mat[vi].insert(i, (vj, val)) 
    
    # 获取边
    def get_edge(self, vi, vj):
        for i, val in self._mat[vi]:
            if i == vj:
                return val
    # 获取出度
    def out_edge(self, vi):
        return self._mat[vi]