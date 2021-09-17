# -*- coding: utf-8 -*-
# @Author   : Just-silent
# @time     : 2020/9/20 19:37

# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        pass

    def minNumberInRotateArray(self, rotateArray):
        s = 0
        e = len(rotateArray) - 1
        if len(rotateArray) == 0:
            return 0
        else:
            while rotateArray[s] >= rotateArray[e]:
                middle = (s + e) // 2
                if rotateArray[s] <= rotateArray[middle]:
                    s = middle
                else:
                    e = middle
            return rotateArray[s]
        # write code here
solution = Solution()
print(solution.minNumberInRotateArray([1,0,1,1,1]))