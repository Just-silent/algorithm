# -*- coding: utf-8 -*-
# @Author   : Just-silent
# @time     : 2021/1/29 10:03

# 找出所有和为S的连续正数序列

class Solution:
    def FindContinuousSequence(self, tsum):
        sum_all = []
        array = [t for t in range(1, tsum)]
        array_i = []
        for i in range(1, tsum-1):
            while i>=0:
                array_i.append(array[i])
                if sum(array_i) == tsum:
                    sum_all.append(array_i[::-1])
                    array_i = []
                    break
                if i==0 and sum(array_i) != tsum:
                    array_i = []
                i-=1
        return sum_all

if __name__ == '__main__':
    solution = Solution()
    tsum = 9
    print(solution.FindContinuousSequence(tsum))
