# -*- coding: utf-8 -*-
# @Author   : Just-silent
# @time     : 2021/1/29 10:03

class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        array2dict = {}
        for x in array:
            if x not in array2dict.keys():
                array2dict[x] = 1
            else:
                array2dict[x] += 1
        result = []
        for x in array2dict.keys():
            if array2dict[x] == 1:
                result.append(x)
        return result

if __name__ == '__main__':
    solution = Solution()
    array = [1, -2, 3, 10, -4, 7, 2, -5]
    print(solution.FindNumsAppearOnce(array))
