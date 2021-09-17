# -*- coding: utf-8 -*-
# @Author   : Just-silent
# @time     : 2021/1/29 10:03

class Solution:
    def Fibonacci(self, n):
        if n==0:
            return 0
        elif n==1:
            return 1
        x = 0
        y = 1
        while n>1:
            z = x+y
            x = y
            y = z
            n-=1
        return y

if __name__ == '__main__':
    n = 4
    solution = Solution()
    print(solution.Fibonacci(n))