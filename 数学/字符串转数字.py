# -*- coding: utf-8 -*-
# @Author   : Just-silent
# @time     : 2021/1/29 10:03

class Solution:
    def StrToInt(self, s):
        if len(s)==0:
            return 0
        s2n = {
            '0':0,
            '1':1,
            '2':2,
            '3':3,
            '4':4,
            '5':5,
            '6':6,
            '7':7,
            '8':8,
            '9':9
        }
        chars = list(s2n.keys())
        num = 0
        c = s[0]
        if s[0] in ['+', '-']:
            s = s[1:]
        l = len(s) -1
        for s_i in s:
            if s_i in chars:
                num+=s2n[s_i]*(pow(10, l))
                l-=1
            else:
                return 0
        if c=='+':
            return num
        elif c=='-':
            return num*-1
        else:
            return num

if __name__ == '__main__':
    s = "123"
    solution = Solution()
    print(solution.StrToInt(s))
