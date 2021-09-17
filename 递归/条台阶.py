# -*- coding: utf-8 -*-
# @Author   : Just-silent
# @time     : 2020/11/29 15:41

# 递归
class Solution:
    def jumpFloor(self, number):
        def jumpKinds(number):
            if number==1:
                return 1
            elif number==2:
                return 2
            else:
                return jumpKinds(number-1)+jumpKinds(number-2)
        return jumpKinds(number)

# 递归+记忆
class Solution:
    def jumpFloor(self, number):
        self.result = [-1]*number
        def jumpKinds(number, result):
            if number==1:
                return 1
            elif number==2:
                return 2
            else:
                if result[number-1]!=-1:
                    return result[number-1]
                else:
                    return jumpKinds(number-1, result)+jumpKinds(number-2, result)
        return jumpKinds(number, self.result)

# 动态规划