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

target = "David json shit sse"
pattern = "json"
location = simple_match(target, pattern)
print(location)