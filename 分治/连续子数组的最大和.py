# -*- coding: utf-8 -*-
# @Author   : Just-silent
# @time     : 2021/1/29 10:03

# 输入一个整型数组，数组里有正数也有负数。数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。要求时间复杂度为 O(n).

class Solution:
    def FindGreatestSumOfSubArray(self, array):
        if len(array) == 1:
            return array[0]
        else:
            max_i = [array[0]] * len(array)
            for i in range(1, len(array)):
                max_i[i] = max(array[i], max_i[i-1] + array[i])
            return max(max_i)
        pass

if __name__ == '__main__':
    solution = Solution()
    array = [1,-2,3,10,-4,7,2,-5]
    print(solution.FindGreatestSumOfSubArray(array))