# -*- coding: utf-8 -*-
# @Author   : Just-silent
# @time     : 2021/1/29 10:03

class Solution:
    def IsContinuous(self, numbers):
        if len(numbers) == 0:
            return False
        mi = 15
        ma = max(numbers)
        zero = 0
        d = {}
        for n in numbers:
            if n == 0:
                zero += 1
            else:
                if n not in d.keys():
                    d[n] = 1
                else:
                    d[n] += 1
            if n < mi and n != 0:
                mi = n
        for k in d.keys():
            if d[k] == -1:
                zero -= 1
            elif d[k] > 1:
                return False
        if ma - mi + 1 - len(numbers) + zero <= zero:
            return True
        else:
            return False

if __name__ == '__main__':
    s = [0,3,2,6,4]
    solution = Solution()
    print(solution.IsContinuous(s))