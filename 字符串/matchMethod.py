def simple_match(target, pattern):
    m, n = len(target), len(pattern)
    i, j = 0, 0
    while i < m and j < n:
        # 如果匹配到字符，模式串和目标串的下标都向前移动
        if target[i] == pattern[j]:
            i, j = i + 1, j + 1
        # 如果有字符不匹配，模式串的下标归零，整体右移一位
        else:
            i, j = i - j + 1, 0
    # 如果模式串的当前下表等于n 循环结束，
    # 模式串所有的字符都匹配到目标串中的对应字符，返回目标串中，子串开始的下标
    if j == n:
        return i - j
    # 未找到匹配，返回-1
    else:
        return -1
"""
    KMP无回溯串匹配算法
"""
def kmpMatch(target, pattern, pNext):
    j, i = 0, 0
    n, m = len(target), len(pattern)
    while j < n and i < m:
        # 匹配到字符，进行下一位的匹配
        if i == -1 or target[j] == pattern[i]: 
            # 模式串与目标串都前进一位
            j, i = j + 1, i + 1
        else:
            # 匹配失败, 考虑pNext决定的下一个字符
            i = pNext[i]
    if i == m:
        return j - i
    else:
        return -1

target = "David json shit sse"
pattern = "json"
location = simple_match(target, pattern)
print(location)