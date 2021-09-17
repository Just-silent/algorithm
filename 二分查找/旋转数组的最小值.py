# -*- coding: utf-8 -*-
# @Author   : Just-silent
# @time     : 2020/11/27 10:33

# -*- coding:utf-8 -*-


class Solution:
    def __init__(self):
        self.low = 0
        self.high = 0
        self.mid = 0
        pass

    def minNumberInRotateArray(self, rotateArray):
        if len(rotateArray) == 0:
            return 0
        else:
            self.low = 0
            self.high = len(rotateArray) - 1
            self.mid = (self.low + self.high) // 2
            while self.high != self.low:
                if rotateArray[self.low] < rotateArray[self.high]:
                    return rotateArray[self.low]
                if rotateArray[self.low] > rotateArray[self.mid]:
                    self.high = self.mid
                elif rotateArray[self.low] < rotateArray[self.mid]:
                    self.low = self.mid + 1
                else:
                    self.low=self.low+1
                self.mid = (self.low + self.high) // 2
            return rotateArray[self.low]
        # write code here


x = input()[1:-1].split(',')
solution = Solution()
print(solution.minNumberInRotateArray(x))

# input [1,0,1,1,1,1]
# output 0