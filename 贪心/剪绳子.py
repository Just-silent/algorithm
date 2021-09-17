# -*- coding: utf-8 -*-
# @Author   : Just-silent
# @time     : 2020/11/28 15:11

class Solution:
    def __init__(self, n):
        self.pre_result = []
        for i in range(n):
            self.pre_result.append(-1)

    def cutRope(self, number):
        if number<=4:
            self.pre_result[number - 1] = number
            return number
        if self.pre_result[number-1]!=-1:
            return self.pre_result[number-1]
        else:
            s = 0
            for i in range(1,number):
                s = max(s, i*self.cutRope(number-i))
            self.pre_result[number-1] = s
            return s
        pass

    def get_result(self, number):
        if number==2:
            return 1
        elif number==3:
            return 2
        else:
            return self.cutRope(number)

number = int(input())
solution = Solution(number)
print(solution.get_result(number))