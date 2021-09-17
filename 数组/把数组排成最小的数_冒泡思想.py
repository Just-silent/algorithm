# -*- coding: utf-8 -*-
# @Author   : Just-silent
# @time     : 2021/1/29 10:03

# 冒泡
class Solution:
    def PrintMinNumber(self, numbers):
        for i in range(len(numbers) - 1):
            for j in range(i + 1, len(numbers)):
                if int(str(numbers[i]) + str(numbers[j])) > int(str(numbers[j]) + str(numbers[i])):
                    numbers[i], numbers[j] = numbers[j], numbers[i]
        return "".join([str(i) for i in numbers])


if __name__ == '__main__':
    solution = Solution()
    numbers = [3,32,321,1151]
    print(solution.PrintMinNumber(numbers))