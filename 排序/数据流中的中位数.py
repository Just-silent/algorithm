# -*- coding: utf-8 -*-
# @Author   : Just-silent
# @time     : 2021/1/23 10:56

# 排序算法
# sort方法

class Solution:
    def __init__(self):
        self.up = []
        pass

    def Insert(self, num):
        self.up.append(num)
        pass

    def buildMaxHeap(self, length):
        for i in range((length-2)//2, -1, -1):
            left = 2*i+1
            index = left
            if 2*i+2<length:
                right = 2*i+2
                if self.up[right]>self.up[left]:
                    index = right
            if self.up[i] < self.up[index]:
                temp = self.up[i]
                self.up[i] = self.up[index]
                self.up[index] = temp
        pass

    def adjust(self, max_index):
        temp = self.up[max_index]
        self.up[max_index] = self.up[0]
        self.up[0] = temp
        for i in range((max_index-1)//2):
            left = 2 * i + 1
            index = left
            if 2 * i + 2 < max_index:
                right = 2 * i + 2
                if self.up[right] > self.up[left]:
                    index = right
            if self.up[i] < self.up[index]:
                temp = self.up[i]
                self.up[i] = self.up[index]
                self.up[index] = temp
        pass

    def GetMedian(self):
        length = len(self.up)
        self.buildMaxHeap(length)
        for i in range((length+1)//2):
            self.adjust(length-i-1)
        if length%2==0:
            return (self.up[length//2]+self.up[length//2-1])/2
        else:
            return self.up[length//2]
        pass

solution = Solution()
arr = [5,2,3,4,1,6,7,0,8]
for a in arr:
    solution.Insert(a)
print(solution.GetMedian())
