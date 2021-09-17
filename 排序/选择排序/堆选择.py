# -*- coding: utf-8 -*-
# @Author   : Just-silent
# @time     : 2021/1/26 14:38

# 思想：1. 初始化大（小）根堆
#       2. 根节点与末尾置换，然后重新构造大（小）根堆
#       3. 知道还剩一个节点

class HeapSort():
    def __init__(self, kind, arr):
        self.arr = arr
        if kind=='up':
            self.buildMaxHeap()
        else:
            self.buildMinHeap()
        for i in range(len(self.arr)-1, 0, -1):
            self.adjust(kind, i)
        pass

    def buildMaxHeap(self):
        for i in range((len(self.arr)-2)//2, -1, -1):
            left = 2*i+1
            index = left
            if 2*i+2 <= len(self.arr)-1:
                right = 2*i+2
                if self.arr[right] > self.arr[left]:
                    index = right
            if self.arr[index] > self.arr[i]:
                temp = self.arr[index]
                self.arr[index] = self.arr[i]
                self.arr[i] = temp
        pass

    def buildMinHeap(self):
        for i in range((len(self.arr) - 2) // 2, -1, -1):
            left = 2 * i + 1
            index = left
            if 2 * i + 2 <= len(self.arr) - 1:
                right = 2 * i + 2
                if self.arr[right] < self.arr[left]:
                    index = right
            if self.arr[index] < self.arr[i]:
                temp = self.arr[index]
                self.arr[index] = self.arr[i]
                self.arr[i] = temp
        pass

    def adjust(self, kind, max_index):
        if kind=='up':
            temp = self.arr[max_index]
            self.arr[max_index] = self.arr[0]
            self.arr[0] = temp
            for i in range(max_index//2):
                left = 2*i+1
                index = left
                if 2*i+2 <= max_index-1:
                    right = 2*i+2
                    if self.arr[right] > self.arr[left]:
                        index = right
                if self.arr[i] < self.arr[index]:
                    temp = self.arr[index]
                    self.arr[index] = self.arr[i]
                    self.arr[i] = temp
        else:
            temp = self.arr[max_index]
            self.arr[max_index] = self.arr[0]
            self.arr[0] = temp
            for i in range(max_index // 2):
                left = 2 * i + 1
                index = left
                if 2 * i + 2 <= max_index - 1:
                    right = 2 * i + 2
                    if self.arr[right] < self.arr[left]:
                        index = right
                if self.arr[i] > self.arr[index]:
                    temp = self.arr[index]
                    self.arr[index] = self.arr[i]
                    self.arr[i] = temp
        pass

    def getMaxOrMin(self):
        return self.arr
        pass

# 时间复杂度：
# 最坏：
# 最好：
# 平均：

# 空间复杂度：O(1)

# 稳定性：


if __name__ == '__main__':
    kind = 'down'
    arr = [5, 2, 7, 4, 4, 9]
    heapSotr = HeapSort(kind, arr)
    arr = heapSotr.getMaxOrMin()
    print(arr)