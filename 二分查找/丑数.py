# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index < 7:
            return index
        p1, p2, p3 = 0, 0, 0
        array = [1]
        while len(array) < index:
            newnum = min(array[p1] * 2, array[p2] * 3, array[p3] * 5)
            array.append(newnum)
            if newnum == array[p1] * 2:
                p1 += 1
            if newnum == array[p2] * 3:
                p2 += 1
            if newnum == array[p3] * 5:
                p3 += 1
        return array[-1]


x = int(input())
solution = Solution()
print(solution.GetUglyNumber_Solution(x))

# 在索引值小于7的时候，前6个丑数为1，2，3，4，5，6，我们设置起始数组为[1]，后面的数依次是对于已知的丑数序列，后面的丑数一定是已知序列中的数字乘以2/3/5得到的。对当前序列中的数字乘2/3/5得到的数字中最小的数字才能放入序列。

# input 7
# output 8