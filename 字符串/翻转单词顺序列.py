# -*- coding: utf-8 -*-
# @Author   : Just-silent
# @time     : 2021/1/29 10:03

class Solution:
    def ReverseSentence(self, s):
        cs = s.split(' ')
        return ' '.join(cs[::-1])

if __name__ == '__main__':
    s = "nowcoder. a am I"
    solution = Solution()
    print(solution.ReverseSentence(s))