# -*- coding: utf-8 -*-
# @Author   : Just-silent
# @time     : 2021/1/29 10:03

class Solution:
    def multiply(self, A):
        n = len(A)
        B = []
        if n == 0:
            return B
        for i in range(n):
            tmp = A[i]
            A[i] = 1
            Bi = 1
            for j in A:
                Bi *= j
            B.append(Bi)
            A[i] = tmp
        return B

if __name__ == '__main__':
    solution = Solution()
    A = [1,2,3,4,5]
    print(solution.multiply(A))