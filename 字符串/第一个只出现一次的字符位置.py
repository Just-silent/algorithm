# -*- coding: utf-8 -*-
# @Author   : Just-silent
# @time     : 2021/1/29 10:03

class Solution:
    def FirstNotRepeatingChar(self, s):
        # ss = []
        # for i in range(len(s)):
        #     for j in range(i + 1, len(s)):
        #         if s[i] == s[j]:
        #             ss.append(s[i])
        # ss = set(ss)
        # for c in s:
        #     if c not in ss:
        #         return s.find(c)
        # return -1
        from collections import OrderedDict
        number2dict = OrderedDict()
        for n in s:
            if n not in number2dict.keys():
                number2dict[n] = 1
            else:
                number2dict[n] += 1
        for c in number2dict.keys():
            if number2dict[c]==1:
                return s.find(c)

if __name__ == '__main__':
    solution = Solution()
    s = 'google'
    print(solution.FirstNotRepeatingChar(s))