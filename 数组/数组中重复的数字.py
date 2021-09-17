# -*- coding: utf-8 -*-
# @Author   : Just-silent
# @time     : 2021/1/29 10:03



class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        from collections import OrderedDict
        n2dict = OrderedDict()
        for n in numbers:
            if str(n) not in n2dict.keys():
                n2dict[str(n)] = 1
            else:
                n2dict[str(n)] += 1
        for key in n2dict.keys():
            if n2dict[key]>1:
                duplication[0] = int(key)
                return True
        return False


if __name__ == '__main__':
    solution = Solution()
    numbers = [6,3,2,0,2,5,0]
    x=[0]
    print(solution.duplicate(numbers,x))