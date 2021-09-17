# -*- coding: utf-8 -*-
# @Author   : Just-silent
# @time     : 2021/1/29 10:03

class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        if n < 0:
            return 0
        count = 0
        i = 1
        while i <= n:
            diviver = i * 10
            count+=(n//diviver) * i+min(max(n%diviver - i + 1, 0), i)
            i*=10
        return count

if __name__ == '__main__':
    solution = Solution()
    n = 13
    print(solution.NumberOf1Between1AndN_Solution(n))
