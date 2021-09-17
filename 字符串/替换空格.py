# -*- coding: utf-8 -*-
# @Author   : Just-silent
# @time     : 2021/1/29 10:03

class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        return s.replace(' ', '%20')

if __name__ == '__main__':
    solution = Solution()
    s = 'a b c'
    print(solution.replaceSpace(s))