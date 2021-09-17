# -*- coding: utf-8 -*-
# @Author   : Just-silent
# @time     : 2021/1/29 10:03

class Solution:
    def reOrderArray(self, array):
        ret = []
        for i in array:
            if i % 2 == 1:
                ret.append(i)
        for i in array:
            if i % 2 == 0:
                ret.append(i)
        return ret

if __name__ == '__main__':
    solution = Solution()
    array = [1,2,3,4,5,6,7]
    print(solution.reOrderArray(array))