# -*- coding: utf-8 -*-
# @Author   : Just-silent
# @time     : 2021/1/29 10:03

def bubble_sort(arr, kind):
    if kind=='up':
        for i in range(len(arr)-1):
            for j in range(len(arr) - 1 - i):
                if arr[j]>arr[j+1]:
                    temp = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = temp
    else:
        for i in range(len(arr) - 1):
            for j in range(len(arr) - 1 - i):
                if arr[j] < arr[j + 1]:
                    temp = arr[j]
                    arr[j] = arr[j + 1]
                    arr[j + 1] = temp
    return arr

# 时间复杂度：
# 最坏：3*（n-1 + n-2 + ...+ 1） =>  O(n^2)
# 最好：O(n^2) 若代码中增加函数判断 数组是否为顺序的 则为O(n)
# 平均：O(n^2)

# 空间复杂度：O(1)

# 稳定性：稳定


if __name__ == '__main__':
    kind = 'down'
    arr = [5, 2, 7, 4]
    arr = bubble_sort(arr, kind)
    print(arr)