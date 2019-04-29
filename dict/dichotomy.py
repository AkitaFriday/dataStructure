"""
    字典的线性表实现
"""

# 自定义异常类
class DictError(ValueError):
    def __init__(self, error):
        self.error = error
    
    def getMessaage(self):
        print("┑(￣Д ￣)┍ 怪我咯: " + self.error)

# 先构造一个字典类
class dictionary:
    def __init__(self, *args):
        # 用一个列表来存储<key, value>数据项
        self.__lists = []
        try:
            if 0 < len(args) < 2:  
                raise DictError("参数错误，格式应该为: args1, args2或参数为空")
            elif len(args) == 2:
                self.__lists.append([args[0], args[1]]) 
        except DictError as de:
            de.getMessaage()
    # 给字典增加一个查询索引器
    def __getitem__(self, key):
        return self.find(key)
    # 索引增加
    def __delitem__(self, key):
        return self.delete(key)
    # 索引删除
    def __setitem__(self, key, value):
        self.append(key, value)
    
    # 输出格式化
    def formatVal(self, lists):
        return "{0} : {1}".format(lists[0], lists[1])

    # 增加新的字典项
    def append(self, key, value):
        try:
            if key == None:
                raise DictError("没有key")
            if value == None:
                raise DictError("没有value")
            self.__lists.append([str(key), value])
        except DictError as de:
            de.getMessaage()
    
    # 查找key对应的value值
    def find(self, key):
        for i in self._dictionary__lists:
            if i[0] == key:
                return i[1]
        return "没有对应的索引"
    # 返回字典数据项的个数
    def item_num(self):
        return len(self._dictionary__lists)
    # 删除指定key与对应的value
    def delete(self, key):
        for i in self._dictionary__lists:
            if i[0] == key:
                self._dictionary__lists.remove(i)
                return "删除成功"
        return "没有对应索引"
    # 检索所有的<key, value>
    def readAll(self):
        read_list = []
        for i in self._dictionary__lists:
            read_list.append(self.formatVal(i))
        return read_list
    # 返回字典目录
    def dict_index(self):
        index_lists = []
        for i in self._dictionary__lists:
            index_lists.append(i[0])
        return index_lists

"""
    二分法检索
"""
def bisearch(dicts, key):
    low, high = 0, len(dicts) - 1
    while low <= high:
        # 获得中点位置
        mid = low + (high - low) // 2        
        # 找到返回
        if key == dicts[mid][0]:
            return dicts[mid][1]
        # 从低半区找
        if key < dicts[mid][0]:
            high = mid - 1
        # 从高半区找
        else:
            low = mid + 1
    return "索引不存在"
