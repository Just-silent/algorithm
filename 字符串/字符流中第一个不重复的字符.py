# -*- coding: utf-8 -*-
# @Author   : Just-silent
# @time     : 2021/1/29 10:03

class Solution:
    def __init__(self):
        self.l = []
    # 返回对应char
    def FirstAppearingOnce(self):
        from collections import OrderedDict
        d = OrderedDict()
        for c in self.l:
            if c not in d.keys():
                d[c] = 1
            else:
                d[c] += 1
        for key in d.keys():
            if d[key]==1:
                return key
        return '#'
        # write code here
    def Insert(self, char):
        # write code here
        self.l.append(char)