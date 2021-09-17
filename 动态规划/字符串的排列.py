# -*- coding: utf-8 -*-
# @Author   : Just-silent
# @time     : 2020/11/29 16:47

class Solution:
    def Permutation(self, ss):
        def get_other(res,ss):
            re = []
            for r in res:
                s=list(ss)
                for c in list(r):
                    s.remove(c)
                re.append(''.join(s))
            return re
            pass
        if len(ss)==0:
            return []
        if len(ss)==1:
            return [ss]
        else:
            res = list(ss)
            other = get_other(res,ss)
            while other[0]!='':
                x = []
                for r,o in zip(res, other):
                    for c in o:
                        if r+c not in x:
                            x.append(r+c)
                res = x
                other = get_other(res, ss)
            return res
s = "aab"
solution = Solution()
print(solution.Permutation(s))