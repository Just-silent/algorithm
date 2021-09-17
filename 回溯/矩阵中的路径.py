# -*- coding: utf-8 -*-
# @Author   : Just-silent
# @time     : 2021/1/29 10:03

# 回溯是一种算法思想，可以用递归实现

class Solution:
    def hasPath(self, matrix, rows, cols, path):
        flag = []
        starts = []
        for i in range(len(matrix)):
            if matrix[i] == path[0]:
                starts.append(i)
        for start in starts:
            un_index = [i for i in range(len(matrix))]
            un_index.remove(start)
            self.get_path(matrix, start, un_index, path[1:], cols, flag)
            if True in flag:
                return True
        return False

    def get_path(self, matrix, start, un_index, path, cols, flag):
        # 当前点、未占用、子路经
        if len(path)>0:
            next_index = [start+cols, start-cols, start+1, start-1]
            for index in next_index:
                if index<len(matrix) and path[0] == matrix[index] and index in un_index:
                    start = index
                    un_index.remove(index)
                    self.get_path(matrix, start, un_index, path[1:], cols, flag)
            flag.append(False)
        else:
            flag.append(True)

if __name__ == '__main__':
    solution = Solution()
    matrix = 'ABCEHJIGSFCSLOPQADEEMNOEADIDEJFMVCEIFGGS'
    rows = 5
    cols = 8
    path = 'SGGFIECVAASABCEHJIGQEM'
    print(solution.hasPath(matrix, rows, cols, path))