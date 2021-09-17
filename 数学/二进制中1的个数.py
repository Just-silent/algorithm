# -*- coding: utf-8 -*-
# @Author   : Just-silent
# @time     : 2021/1/29 10:03

class Solution:
    # def NumberOf1(self, n):
    #     i_s = []
    #     m = n
    #     while True:
    #         i = n//2
    #         j = n%2
    #         i_s.append(j)
    #         n = i
    #         if i==0:
    #             break
    #     if m>0:
    #         x = [0]*(32-len(i_s))
    #         i_s.extend(x)
    #         i_s = i_s[::-1]
    #     else:
    #         x = [0] * (31 - len(i_s))
    #         i_s.extend(x)
    #         i_s.append(1)
    #         for i in range(len(i_s)-1):
    #             if i_s[i]==1:
    #                 i_s[i] = 0
    #             else:
    #                 i_s[i] = 1
    #                 break
    #         i_s = i_s[::-1]
    #     num = 0
    #     for i in i_s:
    #         if i==1:
    #             num+=1
    #     return num
    def NumberOf1(self, n):
        if n < 0:
            return bin(0xFFFFFFFF & n).count('1')
        return bin(n).count('1')

if __name__ == '__main__':
    solution = Solution()
    n = 10
    print(solution.NumberOf1(n))