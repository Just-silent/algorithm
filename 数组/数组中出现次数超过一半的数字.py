# -*- coding: utf-8 -*-
# @Author   : Just-silent
# @time     : 2021/1/29 10:03

class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        result = 0
        number2dict = {}
        for n in numbers:
            if n not in number2dict.keys():
                number2dict[n] = 1
            else:
                number2dict[n] += 1
        half = len(numbers)/2
        for n in number2dict.keys():
            if number2dict[n]>half:
                result = n
        return result

if __name__ == '__main__':
    solution = Solution()
    numbers = [1,2,3,2,2,2,5,4,2]
    print(solution.MoreThanHalfNum_Solution(numbers))
