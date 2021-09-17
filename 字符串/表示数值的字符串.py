# -*- coding: utf-8 -*-
# @Author   : Just-silent
# @time     : 2021/1/29 10:03

class Solution:
    # s字符串
    def isNumeric(self, s):
        flag = 0
        e = 0
        d = 0
        for i in range(len(s)):
            if s[i] == 'e' or s[i] == 'E':
                e = i
            if s[i] == '.':
                d = i
            if i != 0 and (s[i] == '+' or s[i] == '-') and not (s[i-1]=='e' or s[i-1]=='E'):
                return False
            if (i == 0 or i == len(s) - 1) and (s[i] == 'e' or s[i] == 'E'):
                return False
            if s[i] == '.':
                flag += 1
            if (i == 0 or i == len(s) - 1) and s[i] == '.':
                return False
            if s[i].isalpha() and not (s[i]=='e' or s[i]=='E'):
                return False
        if e!=0 and d!=0:
            if e<d:
                return False
        if flag > 1:
            return False
        return True

if __name__ == '__main__':
    solution = Solution()
    s = "3.1416"
    print(solution.isNumeric(s))