# -*- coding: utf-8 -*-
# @Author   : Just-silent
# @time     : 2021/1/27 9:16

class Solution:
    def buildMinHeap(self, input):
        length = len(input)
        for i in range(length//2-1, -1, -1):
            left = 2*i+1
            index = left
            if 2*i+2<length:
                right = 2*i+2
                if input[right] < input[left]:
                    index = right
            if input[index]< input[i]:
                temp = input[index]
                input[index] = input[i]
                input[i] = temp
        return input

    def adjust(self, heap, max_index):
        temp = heap[max_index]
        heap[max_index] = heap[0]
        heap[0] = temp
        for i in range(max_index // 2):
            left = 2 * i + 1
            index = left
            if 2 * i + 2 <= max_index - 1:
                right = 2 * i + 2
                if heap[right] < heap[left]:
                    index = right
            if heap[i] > heap[index]:
                temp = heap[index]
                heap[index] = heap[i]
                heap[i] = temp
        return heap

    def GetLeastNumbers_Solution(self, tinput, k):
        if k>len(input):
            return []
        heap = self.buildMinHeap(tinput)
        for i in range(k):
            heap = self.adjust(heap, len(heap)-i-1)
        result = []
        for i in range(k):
            result.append(heap.pop())
        return result

input = [4,5,1,6,2,7,3,8]
k = 4
solution = Solution()
print(solution.GetLeastNumbers_Solution(input, k))