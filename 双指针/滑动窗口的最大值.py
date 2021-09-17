# -*- coding: utf-8 -*-
# @Author   : Just-silent
# @time     : 2021/1/29 10:03

class Solution:
    def maxInWindows(self, num, size):
        if size>len(num) or size==0:
            return []
        else:
            s = 0
            e = s+size-1
            result = []
            while e<len(num):
                numbers = []
                for i in range(size):
                    numbers.append(num[s+i])
                result.append(max(numbers))
                s+=1
                e+=1
            return result


if __name__ == '__main__':
    num = [2,3,4,2,6,2,5,1]
    size = 3
    solution = Solution()
    print(solution.maxInWindows(num, size))
