# -*- coding: utf-8 -*-
# @Author   : Just-silent
# @time     : 2021/1/29 10:03

class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        result = []
        s_x = 0
        s_y = 0
        w_y = len(matrix[0])-1
        w_x = len(matrix)-1
        while w_x>=0 and w_y>=0:
            if w_y+1<=0:
                break
            for i in range(w_y+1):
                result.append(matrix[s_x][s_y+i])
            if w_x<=0:
                break
            for i in range(w_x):
                result.append(matrix[s_x+i+1][s_y+w_y])
            if w_y<=0:
                break
            for i in range(w_y):
                result.append(matrix[s_x+w_x][s_y+w_y-i-1])
            if w_x-1<=0:
                break
            for i in range(w_x-1):
                result.append(matrix[s_x+w_x-i-1][s_y])
            s_x+=1
            s_y+=1
            w_x-=2
            w_y-=2
        return result

if __name__ == '__main__':
    solution = Solution()
    matrix = [[1,2],[3,4]]
    print(solution.printMatrix(matrix))