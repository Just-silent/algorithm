# -*- coding: utf-8 -*-
# @Author   : Just-silent
# @time     : 2021/1/29 10:03

class Solution:
    def Power(self, base, exponent):
        result = float(1)
        for i in range(abs(exponent)):
            result = result*base
        if exponent>0:
            return result
        else:
            return 1/result

if __name__ == '__main__':
    solution = Solution()
    base = 2
    exponent = -3
    print(solution.Power(base, exponent))