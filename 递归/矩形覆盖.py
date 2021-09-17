# -*- coding: utf-8 -*-
# @Author   : Just-silent
# @time     : 2020/11/29 16:30

# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        if number==0:
            return 0
        elif number==1:
            return 1
        elif number==2:
            return 2
        else:
            pre = 1
            last = 2
            for i in range(3, number+1):
                res = pre + last
                pre = last
                last = res
            return last
        # write code here