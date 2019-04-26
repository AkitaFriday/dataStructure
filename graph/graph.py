# 定义一个大于所有浮点数的值inf, 用来代替无穷大的概念
INF = float("inf")

# 图的通用异常类
class GraphError(ValueError):
    def __init__(self, value):
        self._value = value
    
    def getMessage(self):
        return self._value

"""
    实现邻接矩阵表示一张图
"""
class Graph:
    # mat 参数需要传入一个初始化的方阵，主要是用来确定图的顶点个数
    def __init__(self, mat, unconn=0):
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
    
    # 返回图中顶点的个数
    def vertex_num(self):
        return self._vnum
    
    # 判断下标是否合法
    def _invalid(self, v):
        return 0 > v or v >= self._vnum
    
    # 增加新的边
    def add_edge(self, vi, vj, val=1):
        try:
            if self._invalid(vi) or self._invalid(vj):
                raise GraphError("传入的顶点参数无效，请检查")
            self._mat[vi][vj] = val
        except GraphError as ge:
            print(ge.getMessage())
    
    # 获得边
    def get_edge(self, vi, vj):
        try:
            if self._invalid(vi) or self._invalid(vj):
                raise GraphError("传入的顶点参数无效，请检查")
            return self._mat[vi][vj]
        except GraphError as ge:
            print(ge.getMessage())
    
    # 获得一个顶点的所有出度
    def get_out_edge(self, vi):
        try:
            if self._invalid(vi):
                raise GraphError("传入的顶点参数无效，请检查")
            return self._out_edge(self._mat[vi], self._unconn)
        except GraphError as ge:
            print(ge.getMessage())
    
    # 构建节点表，返回出度的列表, 参数为行数据
    @staticmethod
    def _out_edge(row, unconn):
        edge = []
        for i in range(len(row)):
            if row[i] != unconn:
                edge.append((i, row[i]))
        return edge

