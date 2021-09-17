# -*- coding: utf-8 -*-
# @Author   : Just-silent
# @time     : 2021/1/29 10:03

class Solution:
    def Print(self, pRoot):
        if pRoot==None:
            return []
        result = []
        l = [pRoot]
        flag = False
        while l!=[]:
            r = []
            next_l = []
            for i in range(len(l)):
                r.append(l[i].val)
                if l[i].left!=None:
                    next_l.append(l[i].left)
                if l[i].right!=None:
                    next_l.append(l[i].right)
            if flag:
                result.append(r[::-1])
                flag = False
            else:
                result.append(r)
                flag = True
            l = next_l
        return result