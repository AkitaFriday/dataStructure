"""
    堆排序
"""


def heapSort(elems):
    def siftDown(elems, e, begin, end):
        i, j = begin, begin * 2 + 1
        while j < end:
            if j + 1 < end and elems[j + 1] < elems[j]:
                j += 1
            if e < elems[j]:
                break
            elems[i] = elems[j]
            i, j = j, j * 2 + 1
        elems[i] = e

    end = len(elems)
    for i in range(end // 2, -1, -1):
        siftDown(elems, elems[i], i, end)

    for i in range((end - 1), 0, -1):
        e = elems[i]
        elems[i] = elems[0]
        siftDown(elems, e, 0, i)


elems = [1, 2, 6, 9, 3, 7, 4]

heapSort(elems)
print(elems)
