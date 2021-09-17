# -*- coding: utf-8 -*-
# @Author   : Just-silent
# @time     : 2021/1/29 10:03

# 递归方法

# class Solution:
#     # array 二维列表
#     def Find(self, target, array):
#         flag = []
#         y_len = len(array[0])
#         if array[0]==[] and y_len==0:
#             return False
#         elif array[0][0] == target:
#             return True
#         self.get_flag(0, 0, target, array, flag)
#         if 1 in flag:
#             return True
#         else:
#             return False
#
#     def get_flag(self, x, y, target, array, flag):
#         if 1 in flag:
#             return 1
#         x_len = len(array)
#         y_len = len(array[0])
#         if array[x][y]<target:
#             f = False
#             if x+1<x_len:
#                 flag.append(self.get_flag(x+1, y, target, array, flag))
#                 f = True
#             if y+1<y_len:
#                 flag.append(self.get_flag(x, y+1, target, array, flag))
#                 f = True
#             if f==False:
#                 return 0
#         elif array[x][y]==target:
#             return 1
#         else:
#             return 0

# 二分
class Solution:
    # array 二维列表
    def Find(self, target, array):
        head_x = 0
        head_y = 0
        tail_x = len(array)
        tail_y = len(array[0])
        if tail_x==0 and tail_y == 0:
            return False
        while True:
            mid_x = (head_x + tail_x)//2
            mid_y = (head_y + tail_y)//2
            if array[mid_x][mid_y]==target:
                return True
            elif array[mid_x][mid_y]<target:
                head_x = mid_x
                head_y = mid_y





if __name__ == '__main__':
    solution = Solution()
    target = 15
    array = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
    print(solution.Find(target, array))