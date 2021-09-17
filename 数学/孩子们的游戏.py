# -*- coding: utf-8 -*-
# @Author   : Just-silent
# @time     : 2021/1/29 10:03

class Solution:
    def LastRemaining_Solution(self, n, m):
        if n==0:
            return -1
        student_id = [i for i in range(n)]
        index = 0
        while len(student_id)>1:
            index = (index + m - 1)%len(student_id)
            student_id.remove(student_id[index])
        return student_id[0]

if __name__ == '__main__':
    solution = Solution()
    n = 5
    m = 3
    print(solution.LastRemaining_Solution(n, m))
