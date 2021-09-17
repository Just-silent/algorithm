# -*- coding: utf-8 -*-
# @Author   : Just-silent
# @time     : 2020/11/29 14:41

# -*- coding:utf-8 -*-
class Solution:
    def cutRope(self, number):
        # write code here
        def back_track(n, mark):
            if n <= 4:
                return n
            # 表示当前back_track(n)已经计算过了
            if mark[n] != -1:
                return mark[n]
            res = 0
            for i in range(1, n):
                res = max(res, i * back_track(n - i, mark))
            mark[n] = res
            return res
        # number = 2和3时，实际最大乘积结果并不等于2和3，因为分段数必须大于1，所以需要特判一下
        if number == 2:
            return 1
        elif number == 3:
            return 2
        else:
            mark = [-1] * (number + 1)
            return back_track(number, mark)

number = int(input())
solution = Solution()
print(solution.cutRope(number))