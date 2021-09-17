# -*- coding: utf-8 -*-
# @Author   : Just-silent
# @time     : 2021/1/29 10:03

class Solution:
    def LeftRotateString(self, s, n):
        b = s[:n]
        e = s[n:]
        return e + b

if __name__ == '__main__':
    s = 'abcXYZdef'
    n = 3
    solution = Solution()
    print(solution.LeftRotateString(s, n))